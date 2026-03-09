# # Class
# class Person:
#     name="Sidra"
#     age=21
#     rollno=9
#     occupation="Python developer"
# #Function
#     def info(self):
#         print(f"{self.name} is a {self.occupation}.")

# #Objects
# obj1=Person()
# obj2=Person()
# obj3=Person()
# # print(obj1.name)
# # obj1.name="Pretty girl"
# # print(obj1.name)
# # print(obj1.occupation)
# obj1.name="Pretty girl"
# obj1.occupation="Accountant"
# obj2.name="Malika"
# obj2.occupation="HR"
# obj1.info()
# obj2.info()
# obj3.info()

# class Car:
#     def __init__(self,brand,model,year):
#         self.brand=brand
#         self.model=model
#         self.year=year

#     def display(self):
#         print("Brand Name:",self.brand)
#         print("Model No: ",self.model)
#         print("Year:",self.year)

# a=Car("BMW",7665,2026)
# b=Car("Toyatta",7643,2025)
# a.display()
# b.display()


# #BOOK CLASS
# class Book:
#     def __init__(self,bookname,title,author,price):
#         self.name=bookname
#         self.title=title
#         self.author=author
#         self.price=price

#     def show(self):
#         print("The book name is",self.name)
#         print("The title of the book is",self.title)
#         print("The name of the author is",self.author)
#         print("The price of the book is",self.price)

# obj1=Book("Python ","Education","Sidra",900)
# obj1.author="Pretty girl"
# obj1.show()

# #CLASS MOBILE
# class Mobile:
#     def __init__(self,brand,model,price):
#         self.brand=brand
#         self.model=model
#         self.price=price

#     def show(self):
#         print("Brand name:",self.brand)
#         print("Model:",self.model)
#         print("Price:",self.price)

# a=Mobile("Samsung","S56",2000000)
# b=Mobile("Apple","pro17",500000)
# a.show()
# b.show()


# #CLASS STUDENT
# class Student:
#     def __init__(self,name,rollno,marks):
#         self.name=name
#         self.rollno=rollno
#         self.marks=marks

#     def details(self):
#         print("Name of the student:",self.name)
#         print("Roll no of the student",self.rollno)
#         print("Marks of the student",self.marks)

# S1=Student("Sidra",9,400)
# S2=Student("Masroor",35,300)
# S1.details()
# S2.details()

# #CLASS RECTANGLE
# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width


#     def area(self):
#         print("Area of the Rectangle",self.length*self.width)


# obj1=Rectangle(6,3)
# obj1.width=877
# obj2=Rectangle(76,233)
# obj1.area()
# obj2.area()


# #CLASS ACCOUNT
# class Account:
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance

#     def deposit(self,amount):
#         self.balance=self.balance+amount


#     def show(self):
#         print("Holder Name:",self.name)
#         print("Balance:",self.balance)


# acc1=Account("Sidra",6000000)
# acc1.deposit(90000)
# acc1.show()


# #Assignment no 1:
# class Employee:
#     def __init__(self,name,job,salary):
#         self.name=name
#         self.job=job
#         self.salary=salary

#     def show(self):
#         print("Name:",self.name)
#         print("Job:",self.job)
#         print("Salary:",self.salary)

# e1=Employee("Rizwan","Managing director",800000)
# e2=Employee("Sidra","HR",500000)
# e1.show()
# e2.show()

#Assignment no 02:
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius

#     def area(self):
#         area=3.14*self.radius*self.radius
#        # print("Area of the circle:",3.14*self.radius*self.radius)
#         print("Area of the circle:",area)
    
# a=Circle(4)
# b=Circle(1)
# a.area()
# b.area()


# # #CLASS ACCOUNT
# class Account:
#     def __init__(self,name,balance):
#        self.name=name
#        self.balance=balance

#     def deposit(self,amount):
#         self.balance=self.balance+amount

#     def withdraw(self,amount):
#         if amount>self.balance:
#             print("Insufficent Amount")
#         else:
#             self.balance=self.balance-amount
#     def show(self):
#          print("Holder Name:",self.name)
#          print("Balance:",self.balance)


# acc1=Account("Sidra",600000)
# acc1.deposit(900000)
# acc1.withdraw(100000)
# acc1.show()

# #CLASS TEACHER
# class Student:
#     def __init__(self,name,subject,experience):
#         self.name=name
#         self.subject=subject
#         self.experience=experience

#     def details(self):
#         print("Name of the Teacher:",self.name)
#         print("Subject of the Teacher:",self.subject)
#         print("Experience of the Teacher:",self.experience)

# t1=Student("Sidra","Math",4)
# t2=Student("Masroor","Pyhsics",3)
# t1.details()
# t2.details()


# #CLASS STUDENT
# class Student:
#     def __init__(self,name,eng,urdu,phy,chem):
#         self.name=name
#         self.english=eng
#         self.urdu=urdu
#         self.phy=phy
#         self.chem=chem


#     def show(self):
#         print("Name of the student:",self.name)
#         print("Marks of English:",self.english)
#         print("Marks of Urdu:",self.urdu)
#         print("Marks of Physics:",self.phy)
#         print("Marks of Chemistry:",self.chem)

#     def total(self):
#         t=self.english+self.urdu+self.phy+self.chem
#         print("Total Marks of the student :",t)

#     def average(self):
#         a=(self.english+self.urdu+self.phy+self.chem)/4
#         print("Average Marks of the Student:",a)


#     def grade(self):
#         a=(self.english+self.urdu+self.phy+self.chem)/4
#         if a>=80:
#             print("A Grade")
#         elif a>=60:
#             print("B Grade")
#         elif a>=40:
#             print("C Grade")
#         else:
#             print("Fail")


# obj=Student("Sidra",87,65,70,75)
# obj.show()
# obj.total()
# obj.average()
# obj.grade()
        




# Class (Blueprint for creating student objects)
class Student:

    # Constructor Method (Automatically runs when object is created)
    def __init__(self, name, roll_no, age, course, marks):
        # Attributes / Variables of the class
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.course = course
        self.marks = marks

    # Method (Function inside a class)
    def show_details(self):
        print("----- Student Details -----")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Age:", self.age)
        print("Course:", self.course)
        print("Marks:", self.marks)

    # Method (Function used to calculate grade)
    def result(self):
        if self.marks >= 80:
            grade = "A"
        elif self.marks >= 60:
            grade = "B"
        elif self.marks >= 40:
            grade = "C"
        else:
            grade = "Fail"

        print("Grade:", grade)
        print("---------------------------")


# Object (Instance of the Student class)
s1 = Student("Sidra", 9, 21, "Python Programming", 85)

# Calling methods using object
s1.show_details()
s1.result()