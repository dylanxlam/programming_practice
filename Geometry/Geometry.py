#  File: Geometry.py

#  Description: This program serves as a versatile 
#  geometry utility. It reads input data from a text file, 
#  detailing properties of geometric shapes like points, spheres, 
#  cubes, and cylinders. The program then conducts various 
#  evaluations on these shapes. It determines relationships such 
#  as proximity of points to origins, containment of points within 
#  shapes, inclusion of one shape within another, and intersection 
#  between shapes. The program provides clear and informative responses 
#  to these geometric inquiries, making it a valuable tool for analyzing 
#  spatial configurations.

#  Student Name: Dylan Lam

#  Student UT EID: DXL85

#  Partner Name: Alexander Romero-Barrionuevo

#  Partner UT EID: ANR 3784

#  Course Name: CS 313E

#  Unique Number: 52605

#  Date Created: 9/17/2023

#  Date Last Modified: 9/17/2023

import math
import sys

class Point(object):
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x:.1f}, {self.y:.1f}, {self.z:.1f})"

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

class Sphere(object):
    def __init__(self, x=0, y=0, z=0, radius=1):
        self.center = Point(x, y, z)
        self.radius = radius

    def __str__(self):
        return f"Center: ({self.center.x:.1f}, {self.center.y:.1f}, {self.center.z:.1f}), Radius: {self.radius:.1f}"

    def area(self):
        return 4 * math.pi * (self.radius ** 2)

    def volume(self):
        return (4/3) * math.pi * (self.radius ** 3)

    def is_inside_point(self, p):
        return self.center.distance(p) < self.radius

    def is_inside_sphere(self, other):
        # Calculate the distance between the centers of the two spheres
        distance = self.center.distance(other.center)

        # Check if the given sphere is strictly inside the current sphere
        return (distance + other.radius) < self.radius

    def is_inside_cube(self, a_cube):
        corners = a_cube.get_corners()
        for corner in corners:
            if not self.is_inside_point(corner):
                return False
        return True 

    def does_intersect_sphere(self, other):
            # Calculate the distance between the centers of the two spheres
            distance_between_centers = self.center.distance(other.center)

            if distance_between_centers + min(self.radius, other.radius) < max(self.radius, other.radius):
                return False

            # Check if the spheres have exactly the same center and radius
            if self.center == other.center and self.radius == other.radius:
                return True

            # Check if the distance is less than or equal to the sum of their radii
            if distance_between_centers <= (self.radius + other.radius):
                # If the centers are too close, they may be considered intersecting,
                # even if the distance is very close to the sum of radii, we'll return True
                return True

            # Check if the spheres are completely separate (no intersection)
            if distance_between_centers > (self.radius + other.radius):
                return False

            # Check if one sphere is fully contained within the other
            if self.radius >= (distance_between_centers + other.radius):
                return True

            if other.radius >= (distance_between_centers + self.radius):
                return True

            # Check if the spheres touch each other from outside (tangential intersection)
            if distance_between_centers == (self.radius + other.radius):
                return True

            # If none of the above conditions are met, the spheres partially intersect
            return False

    def does_intersect_cube(self, a_cube):
        return not (abs(self.center.x - a_cube.center.x) > (self.radius + a_cube.side / 2) or
                    abs(self.center.y - a_cube.center.y) > (self.radius + a_cube.side / 2) or
                    abs(self.center.z - a_cube.center.z) > (self.radius + a_cube.side / 2))

    def circumscribe_cube(self):
        # Calculate the side length of the circumscribing cube
        side_length = 2 * self.radius / math.sqrt(3)
        # Create and return a cube with the same center as the sphere and calculated side length
        return Cube(self.center.x, self.center.y, self.center.z, side_length)

class Cube(object):
    def __init__(self, x=0, y=0, z=0, side=1):
        self.center = Point(x, y, z)
        self.side = side

    def __str__(self):
        return f"Center: ({self.center.x:.1f}, {self.center.y:.1f}, {self.center.z:.1f}), Side: {self.side:.1f}"

    def area(self):
        return 6 * (self.side ** 2)

    def volume(self):
        return self.side ** 3
    
    def get_min_corner(self):
        return Point(
            self.center.x - self.side / 2,
            self.center.y - self.side / 2,
            self.center.z - self.side / 2
        )

    def get_max_corner(self):
        return Point(
            self.center.x + self.side / 2,
            self.center.y + self.side / 2,
            self.center.z + self.side / 2
        )
    
    def get_corners(self):
        half_side = self.side / 2
        corners = [
            Point(self.center.x + half_side, self.center.y + half_side, self.center.z + half_side),
            Point(self.center.x + half_side, self.center.y + half_side, self.center.z - half_side),
            Point(self.center.x + half_side, self.center.y - half_side, self.center.z + half_side),
            Point(self.center.x + half_side, self.center.y - half_side, self.center.z - half_side),
            Point(self.center.x - half_side, self.center.y + half_side, self.center.z + half_side),
            Point(self.center.x - half_side, self.center.y + half_side, self.center.z - half_side),
            Point(self.center.x - half_side, self.center.y - half_side, self.center.z + half_side),
            Point(self.center.x - half_side, self.center.y - half_side, self.center.z - half_side),
        ]
        return corners

    def is_inside_point(self, p):
        return (abs(self.center.x - p.x) <= self.side / 2 and
                abs(self.center.y - p.y) <= self.side / 2 and
                abs(self.center.z - p.z) <= self.side / 2)

    def is_inside_sphere(self, a_sphere):
        return a_sphere.center.distance(self.center) + a_sphere.radius <= self.side / 2

    def is_inside_cube(self, a_cube):
        if isinstance(a_cube, Point):
            p = a_cube
            # Check if the point p is strictly inside the Cube.
            half_side = self.side / 2
            return (
                self.center.x - half_side < p.x < self.center.x + half_side and
                self.center.y - half_side < p.y < self.center.y + half_side and
                self.center.z - half_side < p.z < self.center.z + half_side
            )
        elif isinstance(a_cube, Cube):
            other = a_cube
            half_side = self.side / 2
            other_half_side = other.side / 2

            # Check if all eight corners of the other Cube are strictly inside this Cube.
            return (
                self.center.x - half_side < other.center.x - other_half_side and
                self.center.x + half_side > other.center.x + other_half_side and
                self.center.y - half_side < other.center.y - other_half_side and
                self.center.y + half_side > other.center.y + other_half_side and
                self.center.z - half_side < other.center.z - other_half_side and
                self.center.z + half_side > other.center.z + other_half_side
            )


    def does_intersect_cube(self, other):
        return not (abs(self.center.x - other.center.x) > (self.side / 2 + other.side / 2) or
                    abs(self.center.y - other.center.y) > (self.side / 2 + other.side / 2) or
                    abs(self.center.z - other.center.z) > (self.side / 2 + other.side / 2))

    def intersection_volume(self, other):
        if not self.does_intersect_cube(other):
            return 0

        half_side = min(self.side / 2, other.side / 2)
        return half_side ** 3

    def inscribe_sphere(self):
        radius = self.side / 2
        return Sphere(self.center.x, self.center.y, self.center.z, radius)

class Cylinder(object):
    def __init__(self, x=0, y=0, z=0, radius=1, height=1):
        self.center = Point(x, y, z)
        self.radius = radius
        self.height = height

    def __str__(self):
        return f"Center: ({self.center.x:.1f}, {self.center.y:.1f}, {self.center.z:.1f}), Radius: {self.radius:.1f}, Height: {self.height:.1f}"

    def area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def volume(self):
        return math.pi * (self.radius ** 2) * self.height

    def is_inside_point(self, p):
        # Calculate the z-range of points inside the cylinder
        z_range = (
            self.center.z - self.height / 2,
            self.center.z + self.height / 2
        )

        # Check if the point is inside the cylinder
        distance_squared = (p.x - self.center.x) ** 2 + (p.y - self.center.y) ** 2
        return (
            distance_squared <= self.radius ** 2 and
            z_range[0] < p.z < z_range[1]
        )
    

    def is_inside_sphere (self, a_sphere):
        return (a_sphere.center.distance(Point(a_sphere.center.x, a_sphere.center.y, self.center.z)) + a_sphere.radius <= self.radius and
                a_sphere.center.z >= self.center.z and
                a_sphere.center.z <= self.center.z + self.height)

    def is_inside_cube(self, a_cube):
        if isinstance(a_cube, Cube):
            half_side = a_cube.side / 2
            # Calculate the corners of the cube
            corners = [
                Point(a_cube.center.x - half_side, a_cube.center.y - half_side, a_cube.center.z - half_side),
                Point(a_cube.center.x + half_side, a_cube.center.y - half_side, a_cube.center.z - half_side),
                Point(a_cube.center.x - half_side, a_cube.center.y + half_side, a_cube.center.z - half_side),
                Point(a_cube.center.x + half_side, a_cube.center.y + half_side, a_cube.center.z - half_side),
                Point(a_cube.center.x - half_side, a_cube.center.y - half_side, a_cube.center.z + half_side),
                Point(a_cube.center.x + half_side, a_cube.center.y - half_side, a_cube.center.z + half_side),
                Point(a_cube.center.x - half_side, a_cube.center.y + half_side, a_cube.center.z + half_side),
                Point(a_cube.center.x + half_side, a_cube.center.y + half_side, a_cube.center.z + half_side)
            ]

            # Calculate the range of z-values that would be inside the cylinder
            z_range = (
                self.center.z - self.height / 2,
                self.center.z + self.height / 2
            )

            # Check if all eight corners of the cube are inside the cylinder
            for corner in corners:
                if not (
                    (corner.x - self.center.x) ** 2 + (corner.y - self.center.y) ** 2 <= self.radius ** 2 and
                    z_range[0] <= corner.z <= z_range[1]
                ):
                    return False  # One of the corners is not inside, so return False
            return True  # All corners are inside

        else:
            return False  # Input is not a Cube object
    
    def is_inside_cylinder(self, other):
        # Calculate the range of z-values that would be inside this cylinder
        z_range = (
            self.center.z - self.height / 2,
            self.center.z + self.height / 2
        )

        # Calculate the range of z-values for the other cylinder
        other_z_range = (
            other.center.z - other.height / 2,
            other.center.z + other.height / 2
        )

        # Check if the other Cylinder is strictly inside this Cylinder
        return (
            abs(self.center.x - other.center.x) + other.radius < self.radius and
            abs(self.center.y - other.center.y) + other.radius < self.radius and
            z_range[0] < other_z_range[0] and
            z_range[1] > other_z_range[1]
        )

def main():
    # Read input data from standard input
    input_data = sys.stdin.readlines()

    # Initialize a list to store extracted numbers
    numbers = []

    # Iterate through each line of input
    for line in input_data:
        # Split the line by spaces to separate numbers and other characters
        parts = line.split()

        # Extract and convert the numbers to floats
        for part in parts:
            try:
                num = float(part)
                numbers.append(num)
            except ValueError:
                # If conversion to float fails, ignore the part (possibly a comment)
                pass
    
    # read the coordinates of the first Point p and create a Point object 
    point_p = Point(numbers[0], numbers[1], numbers[2])

    # # read the coordinates of the second Point q and create a Point object
    point_q = Point(numbers[3], numbers[4], numbers[5])

    # read the coordinates of the center and radius of sphereA and create a Sphere object
    sphereA = Sphere(numbers[6], numbers[7], numbers[8], numbers[9])

    # read the coordinates of the center and radius of sphereB and create a Sphere object
    sphereB = Sphere(numbers[10], numbers[11], numbers[12], numbers[13])

    # read the coordinates of the center and side of cubeA and create a Cube object 
    cubeA = Cube(numbers[14], numbers[15], numbers[16], numbers[17])

    # read the coordinates of the center and side of cubeB and create a Cube object 
    cubeB = Cube(numbers[18], numbers[19], numbers[20], numbers[21])

    # read the coordinates of the center, radius and height of cylA and create a Cylinder object 
    cylA = Cylinder(numbers[22], numbers[23], numbers[24], numbers[25], numbers[26])

    # read the coordinates of the center, radius and height of cylB and create a Cylinder object
    cylB = Cylinder(numbers[27], numbers[28], numbers[29], numbers[30], numbers[31])
    
    # print if the distance of p from the origin (is / is not) greater than the distance of q from the origin
    distance_p = point_p.distance(Point(0, 0, 0))
    distance_q = point_q.distance(Point(0, 0, 0))
    print(f"Distance of Point p from the origin {'is' if distance_p > distance_q else 'is not'} greater than the distance of Point q from the origin")

    # print if Point p (is / is not) inside sphereA
    print(f"Point p {'is' if sphereA.is_inside_point(point_p) else 'is not'} inside sphereA")

    # print if sphereB (is / is not) inside sphereA
    print(f"sphereB {'is' if sphereA.is_inside_sphere(sphereB) else 'is not'} inside sphereA")

    # print if cubeA (is / is not) inside sphereA
    print(f"cubeA {'is' if sphereA.is_inside_cube(cubeA) else 'is not'} inside sphereA")

    # print if sphereA (does / does not) intersect sphereB
    print(f"sphereA {'does' if sphereA.does_intersect_sphere(sphereB) else 'does not'} intersect sphereB")

    # print if cubeB (does / does not) intersect sphereB
    print(f"cubeB {'does' if sphereB.does_intersect_cube(cubeB) else 'does not'} intersect sphereB")

    # print if the volume of the largest Cube that is circumscribed by sphereA (is / is not) greater than the volume of cylA
    circumscribed_cube_volume = sphereA.circumscribe_cube().volume()
    cylA_volume = cylA.volume()
    print(f"Volume of the largest Cube that is circumscribed by sphereA {'is' if circumscribed_cube_volume > cylA_volume else 'is not'} greater than the volume of cylA")

    # print if Point p (is / is not) inside cubeA
    print(f"Point p {'is' if cubeA.is_inside_point(point_p) else 'is not'} inside cubeA")

    # print if sphereA (is / is not) inside cubeA
    print(f"sphereA {'is' if cubeA.is_inside_sphere(sphereA) else 'is not'} inside cubeA")

    # print if cubeB (is / is not) inside cubeA
    print(f"cubeB {'is' if cubeA.is_inside_cube(cubeB) else 'is not'} inside cubeA")

    # print if cubeA (does / does not) intersect cubeB
    print(f"cubeA {'does' if cubeA.does_intersect_cube(cubeB) else 'does not'} intersect cubeB")

    # print if the intersection volume of cubeA and cubeB (is / is not) greater than the volume of sphereA
    intersection_vol = cubeA.intersection_volume(cubeB)
    sphereA_vol = sphereA.volume()
    print(f"Intersection volume of cubeA and cubeB {'is' if intersection_vol > sphereA_vol else 'is not'} greater than the volume of sphereA")

    # print if the surface area of the largest Sphere object inscribed by cubeA (is / is not) greater than the surface area of cylA
    inscribed_sphere_area = cubeA.inscribe_sphere().area()
    cylA_area = cylA.area()
    print(f"Surface area of the largest Sphere object inscribed by cubeA {'is' if inscribed_sphere_area > cylA_area else 'is not'} greater than the surface area of cylA")

    # print if Point p (is / is not) inside cylA
    print(f"Point p {'is' if cylA.is_inside_point(point_p) else 'is not'} inside cylA")

    # print if sphereA (is / is not) inside cylA
    print(f"sphereA {'is' if cylA.is_inside_sphere(sphereA) else 'is not'} inside cylA")
        
    # print if cubeA (is / is not) inside cylA
    print(f"cubeA {'is' if cylA.is_inside_cube(cubeA) else 'is not'} inside cylA")


if __name__ == '__main__':
    main()