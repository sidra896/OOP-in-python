# #Default Constructor
# class Laptop:
#     def __init__(self):
#         self.brand="Unknown"
#         self.ram="8GB"
#         self.price=0

#     def show(self):
#         print("Brand Name:",self.brand)
#         print("RAM:",self.ram)
#         print("Price:",self.price)

# a=Laptop()
# a.show()


# #Parametrized constuctor
# class Student:
#     def __init__(self,name,rollno,subject):
#         self.name=name
#         self.rollno=rollno
#         self.subject=subject

#     def details(self):
#         print("Name:",self.name)
#         print("Rollno:",self.rollno)
#         print("Subject:",self.subject)


# obj=Student("Sidra",9,"BSCS")
# obj.details()


# #Both Constructors
# class Car:
#     def __init__(self,brand="Unknown",model="Unknown",year=0):
#         self.brand=brand
#         self.model=model
#         self.year=year

#     def show(self):
#         print("Brand",self.brand)
#         print("Model:",self.model)
#         print("Year:",self.year)
#         print("----------")


# a=Car()
# b=Car("BMW","X5",2025)
# c=Car()
# a.show()
# b.show()
# c.show()


# #Decorators
# def decorate(end):
#     def first():
#         print("Welcome to developer Life")
#         end()
#         print("Good Bye")
#     return first

# @decorate
# def greet():
#     print("Sidra")

# greet()

# def decorate(end):
#     def first(a,b):
#         print("Adding of two number")
#         end(a,b)
#         print("Nice practice")
#     return first

# @decorate
# def add(a,b):
#     print(a+b)
# add(98,1)

# def decorate(end):
#         def first(self):
#             print("Welcome to college")
#             end(self)
#             print("Good Bye to college")
#         return first
# class Student:
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno
#     @decorate
#     def show(self):
#         print("Name:",self.name)
#         print("Roll No:",self.rollno)


# obj=Student("Sidra",9)
# obj.show()


# def decorate(end):
#     def first(self):
#         print("Welcome to Student Result")
#         end(self)
#         print("Good Luck for more success")
#     return first

# class Student:
#     def __init__(self,name,m1,m2,m3,m4):
#         self.name=name
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3
#         self.m4=m4
#     @decorate
#     def show(self):
#         print("Name:",self.name)
#         t=self.m1+self.m2+self.m3+self.m4
#         print("Total:",t)
#         a=t/4
#         print("Average:",a)

# obj=Student("Sidra",66,90,95,80)
# obj.show()


# def decorate(end):
#     def first(self):
#         print("Hello to programming World")
#         end(self)
#         print("Good Luck")
#     return first

# class Student:
#     def __init__(self,name):
#         self.name=name
#     @decorate
#     def show(self):
#         print("Name:",self.name)

# obj=Student("Sidra")
# obj.show()


# def decorate(end):
#     def first(self):
#         print("Welcom to the fumction")
#         end(self)
#         print("Thank you for using this fumction")
#     return first

# class Add:
#     def __init__(self,a=0,b=0):
#         self.a=a
#         self.b=b
#     @decorate
#     def show(self):
#         sum=self.a+self.b
#         print("Sum of the two numbers:",sum)
    
# obj=Add()
# obj1=Add(9,2)
# obj.show()
# obj1.show()

# def decorate(end):
#     def first(self):
#         print("Welcome")
#         end(self)
#         print("Have a nice day")
#     return first

# class greet:
#     @decorate
#     def show(self):
#         print("Hello,Sidra")

# obj=greet()
# obj.show()


def decorate(end):
    def first(self,a,b):
        print(f"Method {end.__name__} is running")
        end(self,a,b)
        print(f"Method {end.__name__} is running")
    return first

class Calculator:
    @decorate
    def Add(self,a,b):
        sum=a+b
        print("Sum:",sum)
    @decorate
    def Mullti(self,a,b):
        multi=a*b
        print("Multiply:",multi)

a=Calculator()
a.Add(65,1)
a.Mullti(5,5)







