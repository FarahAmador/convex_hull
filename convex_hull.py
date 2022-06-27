import numpy as np
from scipy.spatial import ConvexHull, convex_hull_plot_2d
import matplotlib.pyplot as plt


def unique_points(points):
    if len(points) != len(set(points)):
        if len(set(points)) < 3:
            raise ValueError("There must be at least three different points")
        else:
            print("Repeated points will be taken as one")
            print(" The points ", points, " are taken like ", list(set(points)))
        n_points = set(points)
    else:
        print("The points ", points, " are unique")
        n_points = points
    return n_points

def area_Heron(points):
    p = points[0]
    q = points[1]
    r = points[2]
    d1 = ((q[1]-p[1])**2 + (q[0]-p[0])**2)**(1.0/2.0)
    d2 = ((r[1]-q[1])**2 + (r[0]-q[0])**2)**(1.0/2.0)
    d3 = ((r[1]-p[1])**2 + (r[0]-p[0])**2)**(1.0/2.0)
    ss = (d1 + d2 + d3) / 2
    area_triangle = (ss *(ss - d1)*(ss - d2)*(ss - d3))** (1.0 / 2.0)
    return area_triangle

def area_vectorial_product_3(n_points):
    l_points = list(n_points)
    if (0,0) in l_points:
        l_points.remove((0,0))
        area_ = abs(np.cross(l_points[0],l_points[1]))
    else:
        area_ = abs(np.cross(l_points[1],l_points[2]))
    return area_

def convex_hull(n_points):
    if len(n_points) < 3:
        raise ValueError("You must enter three non-collinear points")
    if len(n_points) == 3:
        if area_ == 0:
            raise ValueError("Attention: collinear points")
        else:
            print("The area formed is ", area_)
            print ("The convex hull is: ", sorted(l_points))
            hull = sorted(l_points)
            return hull
    if len(n_points) > 3:
        hull = ConvexHull(l_points)
        return (hull)

points = [(0,0), (0,3), (2,0), (0,3)]

n_points = unique_points(points)
l_points = list(n_points)
area_ = area_vectorial_product_3(n_points)
hull = convex_hull(n_points)


#print ("The imput points",  points, "without repeting are ", l_points)
#print(n_points)