import math
class Circle:
    def _init_(self, r):
        self.r = r
class Area(Circle):
    def calArea(self):
        return math.pi * self.r * self.r
class Circumference(Circle):
    def calCirc(self):
        return 2 * math.pi * self.r
r = float(input("Enter radius: "))
a = Area(r)
c = Circumference(r)
print("Area of Circle:", a.calArea())
print("Circumference of Circle:", c.calCirc())
