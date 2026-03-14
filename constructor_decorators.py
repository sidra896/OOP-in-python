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


# def decorate(end):
#     def first(self,a,b):
#         print(f"Method {end.__name__} is running")
#         end(self,a,b)
#         print(f"Method {end.__name__} is running")
#     return first

# class Calculator:
#     @decorate
#     def Add(self,a,b):
#         sum=a+b
#         print("Sum:",sum)
#     @decorate
#     def Mullti(self,a,b):
#         multi=a*b
#         print("Multiply:",multi)

# a=Calculator()
# a.Add(65,1)
# a.Mullti(5,5)


# class Calculator:
#     @decorate
#     def Add(self,a,b):
#         sum=a+b
#         print("Sum:",sum)
#     @decorate
#     def Mullti(self,a,b):
#         multi=a*b
#         print("Multiply:",multi)

# a=Calculator()
# a.Add(65,1)
# a.Mullti(5,5)

# def decorate(end):
#     def first(self,*args,**kwargs):
#         print("Good Morning")
#         end(self,*args,**kwargs)
#         print("Good Bye")
#     return first

# class Teacher:
#     def __init__(self,name=None,subject=None):
#         self.name=name
#         self.subject=subject
#     @decorate
#     def show(self):
#         print("Name:",self.name)
#         print("Subject:",self.subject)

# obj=Teacher()
# obj1=Teacher("Rana Nadeem","Programming")
# obj.show()
# obj1.show()


# # Example: Understanding Python Decorators

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Function execution started...")
        
#         # Calling the original function
#         func(*args, **kwargs)
        
#         print("Function execution finished...")
#     return wrapper


# class Calculator:

#     @decorator
#     def add(self, a, b):
#         result = a + b
#         print("Addition Result:", result)

#     @decorator
#     def multiply(self, a, b):
#         result = a * b
#         print("Multiplication Result:", result)


# # Creating object
# calc = Calculator()

# # Calling methods
# calc.add(10, 5)
# calc.multiply(4, 6)





# #Decorators
# def decorators(end):
#     def first(self):
#         print("Function execution started")
#         end(self)
#         print("Function executuion funished")
#     return first

# #CLass
# class Add:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         #At this ponit we use decorators
#     @decorators
#     def show(self):
#         print("Sum:",self.a+self.b)

# #Object make
# obj=Add(3,8)
# obj.show()



# import time
# def decorators(end):
#     def first(*args,**kwargs):
#         print(f"function {end.__name__} is used")
#         end(*args,**kwargs)
#         print(f"Function {end.__name__} is funished")
#     return first

# def timedeco(end):
#     def first(*args,**kwargs):
#         start=time.time()
#         end(*args,**kwargs)
#         finsh=time.time()
#         print(f"Execution time is {finsh-start} seconds")
#     return first
# class Calculator:
#     @timedeco
#     @decorators
#     def add(self,a,b):
#         print("Sum:",a+b)

#     @timedeco
#     @decorators
#     def subtract(self,a,b):
#         print("Subtraction:",a-b)
#     @timedeco
#     @decorators
#     def multiply(self,a,b):
#         print("Multiplication:",a*b)
    
#     @timedeco
#     @decorators
#     def divide(self,a,b):
#         print("Division:",a/b)

# obj=Calculator()
# obj.add(8,6)
# obj.subtract(8,6)
# obj.multiply(8,6)
# obj.divide(8,6)

# class Student:
#     def __init__(self,name,m1,m2,m3):
#         self.name=name
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3

#     @property    
#     def average(self):
#         avr=self.m1+self.m2+self.m3
#         print("Name:",self.name)
#         print("Average Marks:",avr)
        
    
# obj=Student("Sidra",65,90,54)
# obj.average


# class Calculator:
#     @staticmethod
#     def add(a,b):
#         print("Addition:",a+b)

#     @staticmethod
#     def multi(a,b):
#         print("Multiplication:",a*b)

# obj=Calculator()
# obj.add(8,8)
# obj.multi(8,2)


# class Student:
#     first_name="Sidra"

#     def __init__(self,name):
#         self.name=name

#     @classmethod
#     def nick_first(cls,new_name):
#         cls.first_name=new_name

# obj=Student("Sidra")
# print(Student.first_name)
# Student.nick_first("Semi")
# print(Student.first_name)


# class Bank:
#     bank_name="HBL Bank"
#     def __init__(self,holder_name,balance):
#         self.holder_name=holder_name
#         self.balance=balance

#     @property
#     def info(self):
#         print("Name of the bank:",Bank.bank_name)
#         print("Holder Name:",self.holder_name)
#         print("Balance in Account:",self.balance)
#     @staticmethod
#     def rules():
#         print("Balance in bank account shold be more than 1000")

#     @classmethod
#     def change_bank_name(cls,new_name):
#         cls.bank_name=new_name

# obj=Bank("Sidra",50000000)
# obj.info
# obj.rules()
# Bank.change_bank_name("National Bank")
# print("Updated bank name:",Bank.bank_name)



# class Rectangle:

#     def __init__(self,length,width):
#         self.length=length
#         self.width=width

#     @property
#     def Area(self):
#         print("Area:",self.length*self.width)

#     @staticmethod
#     def info():
#         print("Rectangle has 4 Sides")



# obj=Rectangle(3,4)
# obj.Area
# obj.info()


# class Teacher:
#     school_name="City School"

#     def __init__(self,name,subject):
#         self.name=name
#         self.subject=subject
    
#     @property
#     def show(self):
#         print("School Name:",Teacher.school_name)
#         print("Teacher Name:",self.name)
#         print("Subject:",self.subject)

#     @staticmethod
#     def rules():
#         print("Has to maintain the Rules in Lab")

#     @classmethod
#     def change_school_name(cls,new_name):
#        cls. school_name=new_name

# obj=Teacher("Rana Nadeem","programming")   
# obj.show
# obj.rules()
# Teacher.change_school_name("Govt College Burewala")
# print("School name updated:",Teacher.school_name)



# class Employee:
#     company_name="Technology Base Company"

#     def __init__(self,name,salary,depart):
#         self.name=name
#         self.salary=salary
#         self.depart=depart

#     @property
#     def details(self):
#         print("Company Name:",Employee.company_name)
#         print("Employee Name:",self.name)
#         print("Employee Salary:",self.salary)
#         print("Department of Employee:",self.depart)

#     @staticmethod
#     def rules():
#         print("All Employees must submit weekly reports.")

#     @classmethod
#     def change_company_name(cls,new_name):
#         cls.company_name=new_name



# obj=Employee("Sidra",500000,"Office Managment")
# obj.details
# obj.rules()
# Employee.change_company_name("Tech company")
# print("New Company Name:",Employee.company_name)



# class Library:
#     library_name="City Library"

#     def __init__(self,title,name,price):
#         self.title=title
#         self.name=name
#         self.price=price

#     @property
#     def info(self):
#         print("Library Name:",Library.library_name)
#         print("Title of the Book:",self.title)
#         print("Name of the Author:",self.name)
#         print("Price Of the Book:",self.price)

#     @staticmethod
#     def rules():
#         print("One the book is buy it is not return")

#     @classmethod
#     def change_library_name(cls,new_name):
#         cls.library_name=new_name



# obj=Library("Peer e Kamal","Umera Ahmed",5000)
# obj.info
# obj.rules()
# Library.change_library_name("Public Library")
# print("Updated Library Name:",Library.library_name)









