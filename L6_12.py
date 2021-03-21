#6_12 Multiple objects from on eclass
class my_class_object():
    def __init__(self,n):
        self.__n = n
    def n_is(self):
        return self.__n
    def change_n(self,new_n):
        self.__n = new_n


#Create the object
obj1 = my_class_object("Ringo")
obj2 = my_class_object("Paul")
obj3 = my_class_object("John")

#print the names
print("*"*25)
print(obj1.n_is())
print(obj2.n_is())
print(obj3.n_is())


