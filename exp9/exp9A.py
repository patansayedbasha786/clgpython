class Rectangle:
    def _init_(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
l = int(input("Enter length: "))
w = int(input("Enter width: "))
r = Rectangle(l, w)
print("Area of Rectangle:", r.area())
