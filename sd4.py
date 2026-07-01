import math
class shape:
    def area(self):
        return 0

class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*self.radius*self.radius

class rectangle(shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width

class triangle(shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return 0.5*(self.base*self.height)
c=circle(5)
r=rectangle(4,6)
t=triangle(3,7)
print("circle area",c.area())
print("rectangle area",r.area())
print("triangle area",t.area())
