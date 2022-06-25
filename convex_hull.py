import numpy as np

def slope_(p:tuple, q:tuple, r:tuple):
    slope_1 = (q[1] - p[1]) / (q[0]- p[0])
    slope_2 = (r[1] - q[1]) / (r[0]- q[0])
    slope_3 = (r[1] - p[1]) / (r[0]- p[0])
    a = slope_1 - slope_2
    b = slope_2 - slope_3
    return a,b

def collinear(a,b):
    if a==b:
        print("ATTENTION: collineals points")
    else:
        print("The points form a triangle")
    return 

def area(p, q, r):
    d1 = ((q[1]-p[1])**2 + (q[0]-p[0])**2)**(1.0/2.0)
    d2 = ((r[1]-q[1])**2 + (r[0]-q[0])**2)**(1.0/2.0)
    d3 = ((r[1]-p[1])**2 + (r[0]-p[0])**2)**(1.0/2.0)
    ss = (d1 + d2 + d3) / 2
    area_triangle = (ss *(ss - d1)*(ss - d2)*(ss - d3))** (1.0 / 2.0)
    return area_triangle

def convex_hull_triangle(area_triangle, p, q, r):
    if area_triangle == 0:
        print("That point don't have the requirements to form a convex hull")
    else:
        print("The convex hull is given for"%p,q,r,p)
    return


p = np.array([0,10])
q = np.array ([5, 10])
r = np.array([20,10])

a, b = slope_(p,q,r)
area_triangle = area(p,q,r)

print (collinear(a, b))

print (convex_hull_triangle(area_triangle,p,q,r))