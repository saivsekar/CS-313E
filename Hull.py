
#  File: Hull.py

#  Description:

#  Student Name: Sai Chandrasekar

#  Student UT EID: svc439

#  Partner Name: Reece Mathew

#  Partner UT EID: rtm2244

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 9/25

#  Date Last Modified: 9/26

import sys

import math


class Point (object):
  # constructor
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist(self, other):
    return math.hypot(self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__(self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__(self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__(self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__(self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__(self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__(self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__(self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)

# Input: p, q, r are Point objects
# Output: compute the determinant and return the value


def det(p, q, r):
    # calculates and returns determinant
    return ((q.x*r.y) - (q.y * r.x) + (p.x * q.y) - (p.x*r.y)
            + (p.y * r.x) - (p.y * q.x))


# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull

def convex_hull(sorted_points):
    n = len(sorted_points)  # total number of points

    upper_hull = []          # this chunk adds first and second points to upper hull
    upper_hull.append(sorted_points[0])
    upper_hull.append(sorted_points[1])
    

    for i in range(2, n):  # from the 3RD object in the list to the last
        upper_hull.append(sorted_points[i])

        # at least 3 objects and no right turns
        while len(upper_hull) >= 3 and det(upper_hull[-3], upper_hull[-2], upper_hull[-1]) >= 0:
            del upper_hull[-2]

    lower_hull = []         # this chunk adds last and second to last points to upper hull
    lower_hull.append(sorted_points[-1])
    lower_hull.append(sorted_points[-2])

    for i in range(n-3 , -1, -1): # from 'n-2'nd object to 1st object (taking into account index starts at 0 and range goes to len-1)
        lower_hull.append(sorted_points[i])

        # at least 3 objects and no right turns
        while (len(lower_hull) >= 3 and det(lower_hull[-3], lower_hull[-2], lower_hull[-1]) >= 0):
            del lower_hull[-2]

    del lower_hull[-1]  # this chunk accounts for duplicates
    del lower_hull[0]

    hull = upper_hull + lower_hull

    return hull


# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon

def area_poly(convex_poly):
    det = 0     # initialize det sum variable

    # to account for last determinant x1 y1
    convex_poly.append(convex_poly[0])

    for i in range(len(convex_poly) - 1):  
        # follows formula of x(n)* y(n+1) - y(n)* x(n+1)

        det += (convex_poly[i].x * convex_poly[i+1].y)

        det -= (convex_poly[i].y * convex_poly[i+1].x)

    area = (1/2) * abs(det)
    return area


# Input: no input
# Output: a string denoting all test cases have passed

def test_cases():
    p = Point(0, 0)
    q = Point(1, 1)
    r = Point(2, 3)
    detcheck = det(p,q,r)
    assert detcheck >= 0
 
    return "all test cases passed"


def main():
    # create an empty list of Point objects
    points_list = []

    # read number of points
    line = sys.stdin.readline()
    line = line.strip()
    num_points = int(line)

    # read data from standard input
    for i in range(num_points):
        line = sys.stdin.readline()
        line = line.strip()
        line = line.split()
        x = int(line[0])
        y = int(line[1])
        points_list.append(Point(x, y))

    # sort the list according to x-coordinates
    sorted_points = sorted(points_list)
    sorted_points.sort()

    # get the convex hull
    hull = convex_hull(sorted_points)

    # run your test cases
    test_cases()

    # print the convex hull
    print("Convex Hull")
    for i in hull:
        print(i)

    # get the area of the convex hull
    print()
    area = area_poly(hull)

    # print the area of the convex hull
    print(f'Area of Convex Hull = {area}')

if __name__ == "__main__":
    main()

