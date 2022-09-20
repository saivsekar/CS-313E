#  File: Geometry.py

#  Description:

#  Student Name: Sai Chandrasekar

#  Student UT EID: sv439

#  Partner Name: Reece Mathew

#  Partner UT EID: rtm2244

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 9/13

#  Date Last Modified: 9/13

import math
import sys


class Point (object):
    # constructor with default values
    def __init__(self, x=0, y=0, z=0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    # create a string representation of a Point
    # returns a string of the form (x, y, z)
    def __str__(self):
        return (f'({self.x}, {self.y}, {self.z})')

    # get distance to another Point object
    # other is a Point object
    # returns the distance as a floating point number
    def distance(self, other):
        return math.hypot(self.x - other.x, self.y - other.y, self.z - other.z)

    # test for equality between two points
    # other is a Point object
    # returns a Boolean
    def __eq__(self, other):
        tol = 1.0e-6
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol) and (abs(self.z - other.z) < tol))


class Sphere (object):
    # constructor with default values
    def __init__(self, x=0, y=0, z=0, radius=1):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.center = Point(self.x, self.y, self.z)
        self.radius = float(radius)

    # returns string representation of a Sphere of the form:
    # Center: (x, y, z), Radius: value
    def __str__(self):
        return (f'Center: ({self.x}, {self.y}, {self.z}), Radius: {self.radius}')

    # compute surface area of Sphere
    # returns a floating point number
    def area(self):
        return 4 * math.pi * (self.radius ** 2)

    # compute volume of a Sphere
    # returns a floating point number
    def volume(self):
        return (4/3) * math.pi * (self.radius ** 3)

    # determines if a Point is strictly inside the Sphere
    # p is Point object
    # returns a Boolean
    def is_inside_point(self, p):
        return (self.center.distance(p) < self.radius)

    # determine if another Sphere is strictly inside this Sphere
    # other is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, other):
        distcenter = self.center.distance(other.center)
        return self.radius > (distcenter + other.radius)

    # determine if a Cube is strictly inside this Sphere
    # determine if the eight corners of the Cube are strictly
    # inside the Sphere
    # a_cube is a Cube object
    # returns a Boolean

    def is_inside_cube(self, a_cube):
        distcenter = self.center.distance(a_cube.center)
        distcube = (a_cube.side * math.sqrt(3)/2)
        
        return (distcenter < (self.radius - distcube))

    # determine if a Cube is strictly outside this Sphere
    # determine if the eight corners of the Cube are strictly
    # outside the Sphere
    # a_cube is a Cube object
    # returns a Boolean
    def is_outside_cube(self, a_cube):
        distcenter = self.center.distance(a_cube.center)
        halfdiagcube = (a_cube.side * math.sqrt(3)/2)

        return (distcenter > (self.radius + halfdiagcube))

    # determine if a Cylinder is strictly inside this Sphere
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cyl(self, a_cyl):
        xdist = abs(self.center.x - a_cyl.center.x)
        ydist = abs(self.center.y - a_cyl.center.y)
        zdist = abs(self.center.z - a_cyl.center.z)
        xcheck = self.radius > abs(xdist + a_cyl.radius)  
        ycheck = self.radius > abs(ydist + a_cyl.radius)
        zcheck = self.radius > abs(zdist + a_cyl.height*0.5)
        return (xcheck and ycheck and zcheck)

    #determines if another Sphere is strictly outside this object
    # other is a Sphere object
    # returns a Boolean
    def is_outside_sphere(self, other):
        distcenter = self.center.distance(other.center)
        return (distcenter > (self.radius + other.radius))

    # determine if another Sphere intersects this Sphere
    # other is a Sphere object
    # two spheres intersect if they are not strictly inside
    # or not strictly outside each other
    # returns a Boolean
    def does_intersect_sphere(self, other):
        distcenter = self.center.distance(other.center)
        return ((not self.is_inside_sphere(other)) and (not self.is_outside_sphere(other)))

    # determine if a Cube intersects this Sphere
    # the Cube and Sphere intersect if they are not
    # strictly inside or not strictly outside the other
    # a_cube is a Cube object
    # returns a Boolean
    def does_intersect_cube(self, other):
        distcenter = self.center.distance(other.center)
        return ((not self.is_inside_cube(other)) and (not self.is_outside_cube(other)))

    # return the largest Cube object that is circumscribed
    # by this Sphere
    # all eight corners of the Cube are on the Sphere
    # returns a Cube object
    def circumscribe_cube(self):
        side = (2*self.radius) / (math.sqrt(3))
        CircumCube = Cube(self.center.x, self.center.y, self.center.z, side)
        return CircumCube


class Cube (object):
    # Cube is defined by its center (which is a Point object)
    # and side. The faces of the Cube are parallel to x-y, y-z,
    # and x-z planes.
    def __init__(self, x=0, y=0, z=0, side=1):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.side = float(side)
        self.center = Point(self.x, self.y, self.z)

    # string representation of a Cube of the form:
    # Center: (x, y, z), Side: value
    def __str__(self):
        return (f'Center: ({self.x}, {self.y}, {self.z}), Side: {self.side}')

    # compute the total surface area of Cube (all 6 sides)
    # returns a floating point number
    def area(self):
        return 6 * (self.side ** 2)

    # compute volume of a Cube
    # returns a floating point number
    def volume(self):
        return self.side ** 3

    # get vertices of cube
    # returns a list of 8 tuples
    def get_vertices(self):
        pointlist = [0, 0, 0, 0, 0, 0, 0, 0]
        dist = self.side/2
        pointlist[0] = Point(self.x + dist, self.y + dist, self.z + dist)
        pointlist[1] = Point(self.x + dist, self.y + dist, self.z - dist)
        pointlist[2] = Point(self.x + dist, self.y - dist, self.z + dist)
        pointlist[3] = Point(self.x + dist, self.y - dist, self.z - dist)
        pointlist[4] = Point(self.x - dist, self.y + dist, self.z + dist)
        pointlist[5] = Point(self.x - dist, self.y + dist, self.z - dist)
        pointlist[6] = Point(self.x - dist, self.y - dist, self.z + dist)
        pointlist[7] = Point(self.x - dist, self.y - dist, self.z - dist)

        return pointlist

    # determines if a Point is strictly inside this Cube
    # p is a point object
    # returns a Boolean

    def is_inside_point(self, p):
        s2 = self.side/2
        xcheck = (self.x - s2) < p.x < (self.x + s2)
        ycheck = (self.y - s2) < p.y < (self.y + s2)
        zcheck = (self.z - s2) < p.z < (self.z + s2)
        return xcheck and ycheck and zcheck

    # determine if a Sphere is strictly inside this Cube
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, a_sphere):
        distcenter = self.center.distance(a_sphere.center)
        return (self.side/2) > (distcenter + (a_sphere.radius/2))

    # determine if another Cube is strictly inside this Cube
    # other is a Cube object
    # returns a Boolean

    def is_inside_cube(self, other):
        distcenter = self.center.distance(other.center)
        return (self.side/2) > (distcenter + other.side/2)

    # determine if another Cube is strictly outside this Cube
    # other is a Cube object
    # returns a Boolean
    def is_outside_cube(self, other):
        distcenter = self.center.distance(other.center)
        return (distcenter > (self.side/2 + other.side/2))

    # determine if a Cylinder is strictly inside this Cube
    # a_cyl is a Cylinder object
    # returns a Boolean

    def is_inside_cylinder(self, a_cyl):
        xdist = abs(self.center.x - a_cyl.center.x)
        ydist = abs(self.center.y - a_cyl.center.y)
        zdist = abs(self.center.z - a_cyl.center.z)
        zcheck = self.side/2 > (zdist + a_cyl.radius/2)
        xcheck = self.side/2 > (xdist + a_cyl.radius)
        ycheck = self.side/2 > (ydist + a_cyl.radius)
        return zcheck and xcheck and ycheck

    # determine if another Cube intersects this Cube
    # two Cube objects intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cube object
    # returns a Boolean
    def does_intersect_cube(self, other):

        return ((not self.is_inside_cube(other)) and (not self.is_outside_cube(other)))

    # determine the volume of intersection if this Cube
    # intersects with another Cube
    # other is a Cube object
    # returns a floating point number

    def intersection_volume(self, other):
        if self.does_intersect_cube(other) == False:
            return float(0)
        else:

            if self.x > other.x:
                length = abs((self.x - self.side / 2) -
                             (other.x + other.side / 2))
            else:
                length = abs((other.x - other.side / 2) -
                             (self.x + self.side / 2))

            if self.y > other.y:
                height = abs((self.y - self.side / 2) -
                             (other.y + other.side / 2))
            else:
                height = abs((other.y - other.side / 2) -
                             (self.y + self.side / 2))

            if self.z > other.z:
                width = abs((self.z - self.side / 2) -
                            (other.z + other.side / 2))
            else:
                width = abs((other.z - other.side / 2) -
                            (self.z + self.side / 2))

            return float(length * height * width)

    # return the largest Sphere object that is inscribed
    # by this Cube
    # Sphere object is inside the Cube and the faces of the
    # Cube are tangential planes of the Sphere
    # returns a Sphere object
    def inscribe_sphere(self):
        return Sphere(self.x, self.y, self.z, self.side / 2)


class Cylinder (object):
    # Cylinder is defined by its center (which is a Point object),
    # radius and height. The main axis of the Cylinder is along the
    # z-axis and height is measured along this axis
    def __init__(self, x=0, y=0, z=0, radius=1, height=1):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.radius = float(radius)
        self.height = float(height)
        self.center = Point(self.x, self.y, self.z)

    # returns a string representation of a Cylinder of the form:
    # Center: (x, y, z), Radius: value, Height: value
    def __str__(self):
        return (f'Center: ({self.x}, {self.y}, {self.z}), Radius: {self.radius}, Height: {self.height}')

    # compute surface area of Cylinder
    # returns a floating point number
    def area(self):
        return ((2 * math.pi * self.radius * self.height) + (2 * math.pi * (self.radius**2)))

    # compute volume of a Cylinder
    # returns a floating point number
    def volume(self):
        return math.pi * self.height * (self.radius ** 2)

    # determine if a Point is strictly inside this Cylinder
    # p is a Point object
    # returns a Boolean
    def is_inside_point(self, p):
        hcheck = (self.z - self.height/2) < p.z < (self.z + self.height/2)
        a = Point(p.x, p.y, self.z)
        rcheck = (self.center.distance(a) < self.radius)

        return (hcheck and rcheck)

    # determine if a Sphere is strictly inside this Cylinder
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, a_sphere):
        xdist = abs(self.center.x - a_sphere.center.x)
        ydist = abs(self.center.y - a_sphere.center.y)
        zdist = abs(self.center.z - a_sphere.center.z)
        xcheck = self.radius > (xdist + a_sphere.radius)
        ycheck = self.radius > (ydist + a_sphere.radius)
        zcheck = (self.height/2) > (zdist + a_sphere.radius)

        return (xcheck and ycheck and zcheck)

    # determine if a Cube is strictly inside this Cylinder
    # determine if all eight corners of the Cube are inside
    # the Cylinder
    # a_cube is a Cube object
    # returns a Boolean

    def is_inside_cube(self, a_cube):
        pointlist = a_cube.get_vertices()
        check = False
        for i in pointlist:
            check = self.is_inside_point(i)
            if (check == False):
                break

        return check

    # determine if another Cylinder is strictly inside this Cylinder
    # other is Cylinder object
    # returns a Boolean
    def is_inside_cylinder(self, other):
        xdist = abs(self.center.x - other.center.x)
        ydist = abs(self.center.y - other.center.y)
        zdist = abs(self.center.z - other.center.z)
        xcheck = self.radius > (xdist + other.radius)
        ycheck = self.radius > (ydist + other.radius)
        zcheck = (self.height/2) > (zdist + other.height/2)

        return (xcheck and ycheck and zcheck)

    # determine if another Cylinder is strictly outside this Cylinder
    # other is Cylinder object
    # returns a Boolean
    def is_outside_cylinder(self, other):
        xdist = abs(self.center.x - other.center.x)
        ydist = abs(self.center.y - other.center.y)
        zdist = abs(self.center.z - other.center.z)
        xcheck = xdist > (self.radius + other.radius)
        ycheck = ydist > (self.radius + other.radius)
        zcheck = zdist > (self.height/2 + other.height/2)
        return (xcheck and ycheck and zcheck)

    # determine if another Cylinder intersects this Cylinder
    # two Cylinder object intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cylinder object
    # returns a Boolean

    def does_intersect_cylinder(self, other):
        isinside = self.is_inside_cylinder(other)
        isoutside = self.is_outside_cylinder(other)
        return ((not isinside) and (not isoutside))


def main():
    # read data from standard input
    inputlist = sys.stdin.readlines()
    info = []
    for i in inputlist:
        i.strip()
        info.append(i.split())

    # read the coordinates of the first Point p
    px = info[0][0]
    py = info[0][1]
    pz = info[0][2]

    # create a Point object
    p = Point(px, py, pz)

    # read the coordinates of the second Point q
    qx = info[1][0]
    qy = info[1][1]
    qz = info[1][2]

    # create a Point object
    q = Point(qx, qy, qz)

    # read the coordinates of the center and radius of sphereA
    spAx = info[2][0]
    spAy = info[2][1]
    spAz = info[2][2]
    spAr = info[2][3]

    # create a Sphere object
    sphereA = Sphere(spAx, spAy, spAz, spAr)

    # read the coordinates of the center and radius of sphereB
    spBx = info[3][0]
    spBy = info[3][1]
    spBz = info[3][2]
    spBr = info[3][3]

    # create a Sphere object
    sphereB = Sphere(spBx, spBy, spBz, spBr)

    # read the coordinates of the center and side of cubeA
    cAx = info[4][0]
    cAy = info[4][1]
    cAz = info[4][2]
    cAs = info[4][3]

    # create a Cube object
    cubeA = Cube(cAx, cAy, cAz, cAs)

    # read the coordinates of the center and side of cubeB
    cBx = info[5][0]
    cBy = info[5][1]
    cBz = info[5][2]
    cBs = info[5][3]

    # create a Cube object
    cubeB = Cube(cBx, cBy, cBz, cBs)

    # read the coordinates of the center, radius and height of cylA
    cylAx = info[6][0]
    cylAy = info[6][1]
    cylAz = info[6][2]
    cylAr = info[6][3]
    cylAh = info[6][4]

    # create a Cylinder object
    cylA = Cylinder(cylAx, cylAy, cylAz, cylAr, cylAh)

    # read the coordinates of the center, radius and height of cylB
    cylBx = info[7][0]
    cylBy = info[7][1]
    cylBz = info[7][2]
    cylBr = info[7][3]
    cylBh = info[7][4]

    # create a Cylinder object
    cylB = Cylinder(cylBx, cylBy, cylBz, cylBr, cylBh)

    # print if the distance of p from the origin is greater
    # than the distance of q from the origin

    origin = Point()
    var = "is not"
    if (p.distance(origin) > q.distance(origin)):
        var = "is"

    print(
        f'Distance of Point p from the origin {var} greater than the distance of Point q from the origin')

    # print if Point p is inside sphereA
    var = "is not"
    if (sphereA.is_inside_point(p)):
        var = "is"

    print(f'Point p {var} inside sphereA')

    # print if sphereB is inside sphereA
    var = "is not"
    if (sphereA.is_inside_sphere(sphereB)):
        var = "is"

    print(f'sphereB {var} inside sphereA')

    # print if cubeA is inside sphereA
    var = "is not"
    if (sphereA.is_inside_cube(cubeA)):
        var = "is"

    print(f'cubeA {var} inside sphereA')

    # print if cylA is inside sphereA
    var = "is not"
    if (sphereA.is_inside_cyl(cylA)):
        var = "is"

    print(f'cylA {var} inside sphereA')

    # print if sphereA intersects with sphereB
    var = "does not"
    if (sphereA.does_intersect_sphere(sphereB)):
        var = "does"

    print(f'sphereA {var} intersect sphereB')

    # print if cubeB intersects with sphereB
    var = "does not"
    if (sphereB.does_intersect_cube(cubeB)):
        var = "does"

    print(f'cubeB {var} intersect sphereB')

    # print if the volume of the largest Cube that is circumscribed
    # by sphereA is greater than the volume of cylA
    largecube = sphereA.circumscribe_cube()
    var = "is not"
    if (cylA.volume() < largecube.volume()):
        var = "is"

    print(f'Volume of the largest Cube that is circumscribed by sphereA {var} greater than the volume of cylA')

    # print if Point p is inside cubeA

    var = "is not"
    if (cubeA.is_inside_point(p)):
        var = "is"

    print(f'Point p {var} inside cubeA')

    # print if sphereA is inside cubeA
    var = "is not"
    if (cubeA.is_inside_sphere(sphereA)):
        var = "is"
    print(f'sphereA {var} inside cubeA')

    # print if cubeB is inside cubeA
    var = "is not"
    if (cubeA.is_inside_cube(cubeB)):
        var = "is"
    print(f'cubeB {var} inside cubeA')

    # print if cylA is inside cubeA
    var = "is not"
    if (cubeA.is_inside_cylinder(cylA)):
        var = "is"
    print(f'cylA {var} inside cubeA')

    # print if cubeA intersects with cubeB
    var = "does not"
    if (cubeA.does_intersect_cube(cubeB)):
        var = "does"

    print(f'cubeA {var} intersect cubeB')

    # print if the intersection volume of cubeA and cubeB
    # is greater than the volume of sphereA
    var = "is not"
    if (cubeA.intersection_volume(cubeB) > sphereA.volume()):
        var = "is"

    print(f'Intersection volume of cubeA and cubeB {var} greater than the volume of sphereA')

    # print if the surface area of the largest Sphere object inscribed
    # by cubeA is greater than the surface area of cylA
    var = "is not"
    inscribed = cubeA.inscribe_sphere()
    if (inscribed.area() > cylA.area()):
        var = "is"

    print(f'Surface area of the largest Sphere object inscribed by cubeA {var} greater than the surface area of cylA')

    # print if Point p is inside cylA
    var = "is not"
    if (cylA.is_inside_point(p)):
        var = "is"

    print(f'Point p {var} inside cylA')

    # print if sphereA is inside cylA
    var = "is not"
    if (cylA.is_inside_sphere(sphereA)):
        var = "is"

    print(f'sphereA {var} inside cylA')

    # print if cubeA is inside cylA
    var = "is not"
    if (cylA.is_inside_cube(cubeA)):
        var = "is"

    print(f'cubeA {var} inside cylA')

    # print if cylB is inside cylA
    var = "is not"
    if (cylA.is_inside_cylinder(cylB)):
        var = "is"

    print(f'cylB {var} inside cylA')

    # print if cylB intersects with cylA
    var = "does"
    if (cylA.does_intersect_cylinder(cylB)):
        var = "does not"

    print(f'cylB {var} intersect cylA')


def testmain():
    # method to test stuff, take this out before submission
    cylA = Cylinder(-2.0, 1.0, -3.0, 5.0, 4.0)
    cylB = Cylinder(1.0, 5.0, 3.0, 4.0, 2.0)
    a = cylA.does_intersect_cylinder(cylB)
    print(a)
    pass


if __name__ == "__main__":
    main()
    #testmain()
