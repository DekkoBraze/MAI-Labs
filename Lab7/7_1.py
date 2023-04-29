import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        plt.scatter(self.x, self.y, edgecolors="red")


class Shape(Point):
    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self):
        plt.scatter(self.x, self.y, marker="x", edgecolors="red")

    def is_inside(self, point):
        if self.x == point.x and self.y == point.y:
            return True
        else:
            return False


class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def draw(self):
        ax.add_patch(plt.Circle((self.x, self.y), radius=self.r))

    def is_inside(self, point):
        if self.x - self.r <= point.x <= self.x + self.r and self.y - self.r <= point.y <= self.y + self.r:
            return True
        else:
            return False


class Square(Shape):
    def __init__(self, x, y, length):
        super().__init__(x, y)
        self.length = length

    def draw(self):
        ax.add_patch(plt.Rectangle((self.x, self.y), self.length, self.length))

    def is_inside(self, point):
        if self.x <= point.x <= self.x + self.length and self.y <= point.y <= self.y + self.length:
            return True
        else:
            return False


fig, ax = plt.subplots()
ax.plot(20, 20)

c1 = Circle(0, 5, 10)
c1.draw()
c2 = Circle(1, 2, 4)
c2.draw()

s1 = Square(0, 0, 1)
s1.draw()
s2 = Square(10, 10, 3)
s2.draw()

p1 = Point(1, 4)
p1.draw()
p2 = Point(0, 0)
p2.draw()
p3 = Point(10, 10.5)
p3.draw()

print(c1.is_inside(p1))
print(s1.is_inside(p2))
print(c2.is_inside(p3))

plt.show()
