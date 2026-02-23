# GEOG 676 -  Lab 5
# Aurelius Hermawan
# Date: 2/22/2026

import arcpy

class Toolbox(object):
    def __init__(self):
        self.label = "Toolbox"
        self.alias = ""

        self.tools = [tool]

class tool(object):
    def __init__(self):
        self.label = "Proximity of Buildings"
        self.description = "This tool determines what buildings are nearby a selected building."
        self.canRunInBackground = False
        self.category = "Building Tools"
    
    def getParameterInfo(self):
        param0 = arcpy.Parameter(displayName = "GDB Folder", name = "GDB Folder", datatype = "DEFolder", parameterType = "Required", direction = "Input")
        param1 = arcpy.Parameter(displayName = "GDB Name", name = "GDBName", datatype = "GPString", parameterType = "Required", direction = "Input")
        param2 = arcpy.Parameter(displayName = "Garage CSV File", name = "GarageCSVFile", datatype = "DEFile", parameterType = "Required", direction = "Input")
        param3 = arcpy.Parameter(displayName = "Garage Layer Name", name = "GarageLayerName", datatype = "GPString", parameterType = "Required", direction = "Input")
        param4 = arcpy.Parameter(displayName = "Campus GDB", name = "Campus GDB", datatype = "DEType", parameterType = "Required", direction = "Input")
        param5 = arcpy.Parameter(displayName = "Buffer Distance", name = "BufferDistance", datatype = "GPDouble", parameterType = "Required", direction = "Input")

        params = [param0, param1, param2, param3, param4, param5]
        return params
    
    def isLicensed(self):
        return True
    
    def updateParameters(self, parameters):
        return
    
    def updateMessage(self, parameters):
        return
    
    def execute(self, parameters, messages):
        folder_path = parameters[0].valueAsText
        gdb_name = parameters[1].valueAsText
        gdb_path = folder_path + '\\' + gdb_name
        arcpy.CreateFileGDB_management(folder_path, gdb_name)

        csv_path = parameters[2].valueAsText
        garage_layername = parameters[3].valueAsText
        garages = arcpy.MakeXYEventLayer_management(csv_path, 'X', 'Y', garage_layername)

        inputlayer = garages
        arcpy.FeatureClassToGeodatabase_conversion(inputlayer, gdb_path)
        garagepoints = gdb_path + '\\' + garage_layername

        campus = parameters[4].valueAsText
        campus_buildings = campus + '\Structures'
        buildings = gdb_path + '\\' + 'Buildings'

        arcpy.Copy_management(campus_buildings, buildings)

        spatialref = arcpy.Describe(buildings).spatialReference
        arcpy.Project_management(garagepoints, gdb_path + '\GaragePointsReprojected', spatialref)

        bufferdistance = int(parameters[5].value)
        bufferedGarage = arcpy.Buffer_analysis(gdb_path + '\GaragePointsReprojected', gdb_path + '\GaragePointsBuffered', 150)

        arcpy.Intersect_analysis([bufferedGarage, buildings], gdb_path + '\GarageBuildingsIntersection', 'ALL')

        arcpy.TableToTable_conversion(gdb_path + '\GarageBuildingsIntersection.dbf', r'C:\Users\adher\DevSource\Hermawan-GEOG676\Lab5', 'NearbyBuildings')

        return None