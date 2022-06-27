import numpy as np
from sympy import n_order


def unique_points(points):
    if len(points) != len(set(points)):
        if len(set(points)) < 3:
            raise ValueError("There must be at least three different points")
        else:
            print("Repeated points will be taken as one")
        n_points = set(points)
    else:
        print("The points are unique")
        n_points = points
    return n_points

def area_vectorial_product(n_points):
    l_points = list(n_points)
    if (0,0) in l_points:
        l_points.remove((0,0))
        area_ = abs(np.cross(l_points[0],l_points[1]))
    else:
        area_ = abs(np.cross(l_points[1],l_points[2]))
    return area_

points = [(0,0), (0,3), (2,0), (0,3)]

n_points = unique_points(points)
l_points = list(set(points))
area_ = area_vectorial_product(n_points)

print ("The imput points",  points, "without repeting are ", l_points)
print ("The area of the three points are", area_)

