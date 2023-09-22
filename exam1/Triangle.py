# File: Triangle.py
# Description: A basic 2D Triangle class
# Student Name: Dylan Lam
# Student UT EID: DXL85
# Course Name: CS 313E
# Unique Number: 52605

import sys
import math

class Point(object):
    # constructor
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    # get the distance to another Point object
    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

class Triangle(object): 
    # constructor
    def __init__(self, point_a = Point(), point_b = Point(), point_c = Point()):
        self.a = point_a
        self.b = point_b
        self.c = point_c

    # print a string representation of Triangle
    def __str__(self):
        return f"Triangle with points: A{self.point_a}, B{self.point_b}, C{self.point_c}"
    
    # check if the triangle is similar to another triangle
    def __eq__(self, other):
        self_sides = sorted([self.a.dist(self.b), self.b.dist(self.c), self.c.dist(self.a)])
        other_sides = sorted([other.a.dist(other.b), other.b.dist(other.c), other.c.dist(other.a)])
        return self_sides[0] / other_sides[0] == self_sides[1] / other_sides[1] == self_sides[2] / other_sides[2]
    
    # check if triangle is obtuse or not
    def is_obtuse(self):
        sorted_sides = sorted([self.point_a.dist(self.point_b), self.point_b.dist(self.point_c), self.point_c.dist(self.point_a)])
        return not (round(sorted_sides[0] ** 2 + sorted_sides[1] ** 2, 4) >= round(sorted_sides[2] ** 2,4))
    
    def is_scalene(self):
        sorted_sides = sorted([self.point_a.dist(self.point_b), self.point_b.dist(self.point_c), self.point_c.dist(self.point_a)])
        return sorted_sides[0] != sorted_sides[1] != sorted_sides[2]


# takes a string of coordinates and changes it to a list of Points
def get_points(coords_str):
    coords = [float(c) for c in coords_str.split(" ")]
    return [Point(c[0], c[1]) for c in zip(*[iter(coords)]*2)]

def main():
    # read the two triangles
    pointsA = get_points(sys.stdin.readline().strip())
    pointsB = get_points(sys.stdin.readline().strip())

    triangleA = Triangle(pointsA[0], pointsA[1], pointsA[2])
    triangleB = Triangle(pointsB[0], pointsB[1], pointsB[2])

    # Print final output
    print('A', triangleA)
    print('B', triangleB)

    print('A obtuse', triangleA.is_obtuse())
    print('B obtuse', triangleB.is_obtuse())

    print('A scalene', triangleA.is_scalene())
    print('B scalene', triangleB.is_scalene())

    print('A equals b', triangleA == triangleB)

if __name__ == "__main__":
    main()