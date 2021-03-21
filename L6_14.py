#6_14 Subclass the rectangle class with a square class
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

class Square(Rectangle):
    def __init__(self,length):
        super().__init__(length,length)

#create the new subclassed object
print('*' * 20)
sq1 = Square(8)
print(sq1.area())
