import math

class Rectangle(object):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
        
class Square(Rectangle):
    def __init__(self,width):
        self.width=width
        self.height=width

class Ellipse(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def area(self):
        return math.pi*self.a*self.b

class Circle(Ellipse):
    def __init__(self,r):
        self.a=r
        self.b=r

def compute_area(shapes):
    return sum(i.area() for i in shapes)


shapes=[Ellipse(10,20),Square(15),Circle(5),Rectangle(20,15),Circle(5),Square(15),
Ellipse(10,20)]
total_area=compute_area(shapes)
print(total_area)
