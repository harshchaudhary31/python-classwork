import math


class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, otherpoint):
        x1 = self.x
        y1 = self.y
        x2 = otherpoint.x
        y2 = otherpoint.y
        d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        return d


p1 = point(0, 1)
p2 = point(2, 4)
p3 = point(3, 6)
p4 = point(7, 7)


print(p1.distance(p2))
print(p2.distance(p1))
