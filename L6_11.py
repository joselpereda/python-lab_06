#6_11 Class with private variables
class my_class_object():
    def __init__(self,n):
        self.__n = n
    def n_is(self):
        return self.__n
    def change_n(self,new_n):
        self.__n=new_n

#create the object
obj1 = my_class_object("Betty")
obj2 = my_class_object("Bob")

print(obj1)

