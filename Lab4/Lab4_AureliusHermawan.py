# GEOG 676 -  Lab 4
# Aurelius Hermawan
# Date: 2/15/2026

import arcpy

buffer_distance = input("Please enter your desired buffer distance: ")

arcpy.env.workspace = r'C:\\Users\\adher\\DevSource\\Hermawan-GEOG676\\Lab4\\env_codes'
folder_path = r'C:\\Users\\adher\\DevSource\\Hermawan-GEOG676\\Lab4'
gdb_name = 'Test.gdb'
gdbpath = folder_path + '\\' + gdb_name
arcpy.CreateFileGDB_management(folder_path, gdb_name)

csvpath = r'C:\\Users\\adher\\DevSource\\Hermawan-GEOG676\\Lab4\\Garages.csv'
garage_lyr_name = 'GaragePoints'
garages = arcpy.MakeXYEventLayer_management(csvpath, 'X', 'Y', garage_lyr_name)

input_lyr = garages
arcpy.FeatureClassToGeodatabase_conversion(input_lyr, gdbpath)
garage_points = gdbpath + '\\' + garage_lyr_name

campus = r'C:\\Users\\adher\\DevSource\\Hermawan-GEOG676\\Lab4\\Campus.gdb'
campusbuildings = campus + '\\Structures'
buildings = gdbpath + '\\' + '\\Buildings'

arcpy.Copy_management(campusbuildings, buildings)

spatialref = arcpy.Describe(buildings).spatialReference
arcpy.Project_management(garage_points, gdbpath + '\GaragePoints_Reprojected', spatialref)

garagebuffered = arcpy.Buffer_analysis(gdbpath + '\GaragePoints_Reprojected', gdbpath + '\GaragePoints_Buffered', buffer_distance)

arcpy.Intersect_analysis([garagebuffered, buildings], gdbpath + '\Garage_BuildingIntersect', 'ALL')

arcpy.TableToTable_conversion(gdbpath + '\Garage_BuildingIntersect.dbf', 'C:\\Users\\adher\\DevSource\\Hermawan-GEOG676\\Lab4', 'NearBuildings.csv')