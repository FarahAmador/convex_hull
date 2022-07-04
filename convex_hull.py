from enum import unique
import numpy as np
from scipy.spatial import ConvexHull, convex_hull_plot_2d
import matplotlib.pyplot as plt


def unique_points(points):
    u_points = np.unique(points, axis=0)
    if len(points) != len(u_points):
        if len(u_points) < 3:
            raise ValueError("There must be at least three different points")
        else:
            print("Repeated points will be taken as one")
            print(" The points ", points, " seen as unique are ", u_points)
    else:
        print("The points ", points, " are unique")
    return u_points

def area_vectorial_product_3(u_points):
    area_ = abs(np.cross(u_points[1],u_points[2]))
    return area_

def convex_hull(u_points):
    if len(u_points) < 3:
        raise ValueError("You must enter three non-collinear points")
    if len(u_points) == 3:
        if area_ == 0:
            raise ValueError("Attention: collinear points")
        else:
            print("The area formed is ", area_)
            print ("The convex hull is: ", u_points)
            hull = ConvexHull(u_points)
            return hull
    if len(u_points) > 3:
        hull = ConvexHull(u_points)
        return hull
        
points = np.array([[0.01,0], [2,-3], [-20.,0.005], [2,54], [4,6], [7,12]])

u_points = unique_points(points)

p = u_points[0]
q = u_points[1]
r = u_points[2]

area_ = area_vectorial_product_3(u_points)
hull = convex_hull(u_points)

plt.plot(points[:,0], points[:,1], 'o')
for simplex in hull.simplices:
    plt.plot(u_points[simplex, 0], u_points[simplex, 1], 'k-')

plt.plot(u_points[hull.vertices,0], u_points[hull.vertices,1], 'r--', lw=2)
plt.plot(u_points[hull.vertices[0],0], u_points[hull.vertices[0],1], 'ro')
plt.show()

#print ("The imput points",  points, "without repeting are ", l_points)
#print(n_points)