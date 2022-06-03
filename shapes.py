


class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius**2
    def circumference(self):
        return 2*3.14*self.radius
class Square: 
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side**2
    def calculate_the_perimeter(self):
        return 4*self.side
class Rectangle:
    def __init__(self,width,length):
        self.width = width
        self.length = length
    def calculate_the_area(self):
        area = self.width*self.length
        return area
    def calculate_the_perimeter(self):
        perimeter = self.length + self.width
        return 2*perimeter

class Sphere:
    def __init__(self,radius):
        self.radius = radius
    def surface_area(self):
        area = 4*3.14*self.radius**2
        return area
    def calculate_the_volume(self):
        volume = (4/3)*3.14*self.radius*self.radius*self.radius
        return volume


    



