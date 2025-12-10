#Class and Object Representation in Python
'''
class Student():
    name = "Prince"
    age = 20
s1 = Student()

print("Name:", s1.name)
print("Age:", s1.age)   

'''    
#Contructor Method
'''class Laptop():
    def __init__(self):
        print("Laptop constructor ")
    def show(self):
        print("Display")
obj = Laptop()
print(obj.show())'''
# My Test Class 
'''class Test_names():
    def __init__(self):
        print("Ajay - My Name")
    def show(self):
        print("Bad - Mood")
obj = Test_names()
print(obj.show())'''
#writing a class with constructor method - > with multiple parameters instead of def __init_(self):-> twice
#and for ur information py only reads the last constructor value so using this method we can pass multiple defs

#MULTIPLE DEF CLASSES AT ONCE SO MULTipLE CONSTRUCTOR 

'''class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"name:{self.name}, age:{self.age}")
s1 = Student("Prince", 20)
s1.display()
s2 = Student("Ajay", 22)
s2.display()'''