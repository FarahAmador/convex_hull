import numpy as np

def area(p, q, r):
    d1 = ((q[1]-p[1])**2 + (q[0]-p[0])**2)**(1.0/2.0)
    d2 = ((r[1]-q[1])**2 + (r[0]-q[0])**2)**(1.0/2.0)
    d3 = ((r[1]-p[1])**2 + (r[0]-p[0])**2)**(1.0/2.0)
    ss = (d1 + d2 + d3) / 2
    area_triangle = (ss *(ss - d1)*(ss - d2)*(ss - d3))** (1.0 / 2.0)
    return area_triangle

def convex_hull(points):
    if len(points) < 3:
        raise ValueError("sdadsad")
    if len(points) > 3:
        raise ValueError("Not implemented yet")
    if area(points[0], points[1], points[2]) == 0:
        raise ValueError("Points are collinear")
    return [0, 1, 2]


p = np.array([0,10])
q = np.array ([5, 10])
r = np.array([20,10])

a, b = slope_(p,q,r)
area_triangle = area(p,q,r)

print (collinear(a, b))

print (convex_hull_triangle(area_triangle,p,q,r))