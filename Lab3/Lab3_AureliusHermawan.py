# GEOG 676 -  Lab 3
# Aurelius Hermawan
# Date: 2/8/2026

# Define classes

class Shape():
    def __init__(self):
        pass

class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w
    def getArea(self):
        return self.length * self.width
    
class Circle():
    def __init__(self, r):
        self.radius = r
    def getArea(self):
        return 3.14 * self.radius * self.radius
    
class Triangle():
    def __init__(self, b, h):
        self.base = b
        self.height = h
    def getArea(self):
        return 0.5 * self.base * self.height

# Read the text file
file = open(r'C:\Users\adher\DevSource\Hermawan-GEOG676\Lab3\shape.txt', 'r')
lines = file.readlines()
file.close()

for line in lines:
    elements = line.split(',')
    shape = elements[0]

    if shape == 'Rectangle':
        rec = Rectangle(int(elements[1]), int(elements[2]))
        print("The area of the rectangle is ", rec.getArea())
    elif shape == 'Circle':
        cir = Circle(int(elements[1]))
        print("The area of the circle is ", cir.getArea())
    elif shape == 'Triangle':
        tri = Triangle(int(elements[1]), int(elements[2]))
        print("The area of the triangle is ", tri.getArea())
    else:
        pass