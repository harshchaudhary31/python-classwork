import math

coordinates = [[0, 1], [2, 4], [3, 6], [7, 7]]


def distanceCacl(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    return ((x2 - x1) ^ 2 + (y2 - y1) ^ 2) ** 1 / 2


def polar(p1):
    x, y = p1
    r = math.sqrt(x**2 + y**2)

    phi = math.degrees(math.atan2(y, x))

    return (r, phi)


def move(p1, displacement):
    moved = {"x": p1["x"] + displacement[0], "y": p1["y"] + displacement[1]}
    return moved


print(distanceCacl([0, 1], [2, 4]))
print(polar([1, 0]))
