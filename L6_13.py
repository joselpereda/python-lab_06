#P_13 Base Class
class Rectangle():
    def __init__(self,l,w):
        self.__length = l
        self.__width = w
    def area(self):
        return self.__length * self.__width
    def change_length(self,l):
        self.__length = l
    def change_width(self,w):
        self.__width = w

area1 = Rectangle(10, 20)
area2 = Rectangle(10, 100)

print("*" * 19)
print("** " + str(area1.area()))
print("** " + str(area2.area()))

