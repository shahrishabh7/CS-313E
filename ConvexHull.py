#  File: Hull.py

#  Description: A convex hull is the smallest convex polygon that will enclose a set of points. In a convex polygon a line joining any two
#  points in the polygon will lie completely within the polygon. One way to visualize a convex hull is as follows: imagine there are nails
#  sticking out over the distribution of points. Place a rubber band such that it encircles all the nails. The figure described by the rubber
#  band is a convex hull.

#  This program will read in a set of points and accordingly print the vertices of the convex hull starting at the extreme left point and going clockwise

#  Student Name:Rishabh Shah

import math

class Point (object):
  # constructor
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    # get the distance to another Point object
    def dist (self, other):
        return math.hypot (self.x - other.x, self.y - other.y)

    # string representation of a Point
    def __str__ (self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    # equality tests of two Points
    def __eq__ (self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

    def __ne__ (self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

    def __lt__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
          if (abs(self.y - other.y) < tol):
            return False
          else:
            return (self.y < other.y)
        return (self.x < other.x)

    def __le__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
          if (abs(self.y - other.y) < tol):
            return True
          else:
            return (self.y <= other.y)
        return (self.x <= other.x)

    def __gt__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
          if (abs(self.y - other.y) < tol):
            return False
          else:
            return (self.y > other.y)
        return (self.x > other.x)

    def __ge__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
          if (abs(self.y - other.y) < tol):
            return True
          else:
            return (self.y >= other.y)
        return (self.x >= other.x)

# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det (p, q, r):
    return (p.x * (q.y - r.y)) + (q.x * (r.y - p.y)) + (r.x * (p.y - q.y))

# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull (sorted_points):
    points = sorted_points
    data_size = len(sorted_points)
    
    upper = []
    upper.append(points[0])
    upper.append(points[1])
    for i in range(2,data_size):
        upper.append(points[i])
        while (len(upper) >= 3) and (det(upper[-3], upper[-2], upper[-1]) >= 0):
            upper.pop(-2)

    lower = []
    lower.append(points[data_size-1])
    lower.append(points[data_size-2])
    for i in range(data_size-3, -1, -1):
        lower.append(points[i])
        while (len(lower) >= 3) and (det(lower[-3], lower[-2], lower[-1]) >= 0):
            lower.pop(-2)
    lower.pop(0)
    lower.pop(-1)

    convex_hull = []

    for x in upper:
        convex_hull.append(x)

    for x in lower:
        convex_hull.append(x)

    return convex_hull

# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly (convex_poly):
    data_size = len(convex_poly)
    n = len(convex_poly)-1
    sum = 0

    pos_x = []
    pos_y = []
    neg_x = []
    neg_y = []

    for x in range(data_size):
        pos_x.append(convex_poly[x].x)
        if x != n:
            pos_y.append(convex_poly[x+1].y)
        else:
            pos_y.append(convex_poly[0].y)

    for x in range(data_size):
        neg_y.append(convex_poly[x].y)
        if x != n:
            neg_x.append(convex_poly[x+1].x)
        else:
            neg_x.append(convex_poly[0].x)

    pos_sum = 0
    for pos in range(data_size):
        sum = pos_x[pos] * pos_y[pos]
        pos_sum += sum

    neg_sum = 0
    for neg in range(data_size):
        sum = neg_y[neg] * neg_x[neg]
        neg_sum -= sum

    total = pos_sum + neg_sum
    total = math.fabs(total) / 2
    return total

def main():
    # create an empty list of Point objects
    points = []

    # read data from standard input
    data = open("hull.in", "r")
    data_size = int(data.readline())
    coord = []

    # read line by line, create Point objects and store in a list
    for x in range(data_size):
        line = data.readline().strip("\n").split("\t")
        line[0], line[1] = int(line[0]), int(line[1])
        points.append(Point(line[0], line[1]))

    # sort the list according to x-coordinates
    temp = None
    counter = 1
    while counter != (data_size-1):
        if points[counter].x > points[counter+1].x:
            temp = points[counter]
            points[counter], points[counter+1] = points[counter+1], temp
            counter = 0
        else:
            counter += 1

    # get the convex hull
    chull = convex_hull(points)
    
    # print your results to standard output
    print("Convex Hull")

    # print the convex hull
    for x in chull:
        print(x)

    # get the area of the convex hull
    chullarea = area_poly(chull)

    # print the area of the convex hull
    print("\nArea of Convex Hull = {}".format(chullarea))

    data.close()

if __name__ == "__main__":
  main()
