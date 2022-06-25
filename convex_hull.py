


def slope(p[0], p[1], q[0], q[1], r[0], r[1]):
    slope_1 = (q[1] - p[1]) / (q[0]- p[0])
    slope_2 = (r[1] - q[1]) / (r[0]- q[0])
    slope_3  = (r[1] - p[1]) / (r[0]- p[0])
    return slope_1, slope_2, slope_3

p = [0,2]
q = (5, 2)
s = (7, 2)

print(slope_1)
print(slope_2)