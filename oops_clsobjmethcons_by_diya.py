# oops class,object

# class Student:
#     name="mariyam"               attribute
#     age=21

# student1=Student()
# print(student1.name)
# print(student1.age)

# oops method

# class Student:
#     def study(self):
#         print("student is studying")
# student1=Student()
# student1.study()

# oops constuctors

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def study(self):
#         print(self.name,"is studying")
# student1=Student("mariyam",21)
# student2=Student("diya",22)
# student3=Student("pooja",20)
# print(student1.name)
# print(student1.age)
# print(student2.name)
# print(student2.age)
# print(student3.name)  
# print(student3.age)     


# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def study(self):
#         print(self.name,"is studying")
#     def display(self):
#         print("name : ",self.name)
#         print("age : ",self.age)

# student1=Student("mariyam",21)
# student2=Student("diya",22)
# student3=Student("pooja",20)

# student1.display()
# student1.study()

# print()
# student2.display()
# student2.study()

# print()
# student3.display()
# student3.study()





# INHERITANCE (TYPES) AND ENCAPSULATION 



# INHERITANCE -----> ഒരു class-ൽ ഉള്ള properties and methods മറ്റൊരു class-ൽ 
# ഉപയോഗിക്കാൻ അനുവദിക്കുന്ന OOP feature ആണ് Inheritance.
#  ഒരു Parent-ന് ചില qualities ഉണ്ട്.
# അത് Child-ലും കാണാം.
# EXAMPLE

# class Animal:
#     def eat(self):
#         print("Animal is eating")

# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")

# d = Dog()

# d.eat()
# d.bark()                       


# TYPES OF INHERITANCE

# .SINGLE INHERITANCE  -----> എന്നാൽ ഒരു Parent class-ിൽ നിന്ന് ഒരു 
# Child class features എടുക്കുന്നതാണ്.
#         ഉദാഹരണത്തിന്, Animal ആണ് Parent class, Dog ആണ് Child class.
# Animal-ന് eat() എന്ന ഒരു method ഉണ്ട്. Dog, Animal-നെ inherit ചെയ്തതിനാൽ
# Dog-നും eat() ഉപയോഗിക്കാൻ കഴിയും. Dog-ന് സ്വന്തമായി bark() എന്ന method-ഉം ഉണ്ടാക്കാം.

# class Animal:
#     def eat(self):
#         print("Animal is eating")

# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")

# d = Dog()
# d.eat()
# d.bark()


# .MULTIPLE INHERITANCE -----> Multiple Inheritance എന്നാൽ ഒരു Child class 
# രണ്ട് അല്ലെങ്കിൽ അതിൽ കൂടുതൽ Parent classes-ൽ നിന്ന് features എടുക്കുന്നതാണ്.
# ഉദാഹരണത്തിന് Father-ന് driving അറിയാം, Mother-ന് cooking അറിയാം.
# Child രണ്ട് പേരിൽ നിന്നും features എടുക്കുന്നു.


# class Father:
#     def driving(self):
#         print("Driving")

# class Mother:
#     def cooking(self):
#         print("Cooking")

# class Child(Father, Mother):
#     pass

# c = Child()
# c.driving()
# c.cooking()


# .MULTILEVEL INHERITANCE   ----->Multilevel Inheritance എന്നാൽ inheritance 
# ഒരു level കഴിഞ്ഞ് അടുത്ത level-ലേക്ക് പോകുന്നതാണ്.
# ഉദാഹരണം:
# Grandfather → Father → Son
# Grandfather-ന്റെ feature Father-ന് കിട്ടുന്നു. Father-ന്റെ 
# feature Son-നും കിട്ടുന്നു.

# class Grandfather:
#     def house(self):
#         print("Grandfather has a house")

# class Father(Grandfather):
#     pass

# class Son(Father):
#     pass

# s = Son()
# s.house()

#  Grandparent → Parent → Child = Multilevel Inheritance.


# .HIERARCHICAL INHERITANCE ------> Hierarchical Inheritance എന്നാൽ ഒരു
#  Parent class-ൽ നിന്ന് ഒന്നിലധികം Child classes features എടുക്കുന്നതാണ്.
# ഉദാഹരണം:
# Animal → Dog
# Animal → Cat
# Dog-നും Cat-നും Animal-ന്റെ eat() method ഉപയോഗിക്കാം.

# class Animal:
#     def eat(self):
#         print("Animal is eating")

# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")

# class Cat(Animal):
#     def meow(self):
#         print("Cat is meowing")

# d = Dog()
# c = Cat()

# d.eat()
# d.bark()

# c.eat()
# c.meow()

# ഇവിടെ ഒരു Parent ആണ് — Animal.
# അതിൽ നിന്ന് രണ്ട് Children ആണ് — Dog, Cat.
# One Parent → Many Children = Hierarchical Inheritance

# .HYBRID INHERITANCE ----->Hybrid Inheritance എന്നാൽ രണ്ടോ 
# അതിലധികമോ types of inheritance ഒരുമിച്ച് ഉപയോഗിക്കുന്നതാണ്.
# അതിനാൽ Hybrid-നെ ഒരു combination of inheritance types എന്ന് പറയാം.

    #    A
    #   / \                              A → B and A → C → Hierarchical
    #  B   C                             B + C → D → Multiple
    #   \ /
    #    D


# class A:
#     def show_a(self):
#         print("A")

# class B(A):
#     def show_b(self):
#         print("B")

# class C(A):
#     def show_c(self):
#         print("C")

# class D(B, C):
#     def show_d(self):
#         print("D")

# d = D()

# d.show_a()
# d.show_b()
# d.show_c()
# d.show_d()


# ENCAPSULATION ------>ഒരു class-ന്റെ ഉള്ളിൽ data-യും methods-ഉം ഒരുമിച്ച് 
# വയ്ക്കുകയും, data-യെ protect ചെയ്യുകയും ചെയ്യുന്നതാണ് Encapsulation.
# Simple example:
# നമ്മുടെ ATM PIN മറ്റുള്ളവർക്ക് കാണാൻ പറ്റില്ലല്ലോ.
# PIN ഒരു protected information ആണ്.
# അതുപോലെ Python-ലും important ആയ data നേരിട്ട് access ചെയ്യാതെ 
# protect ചെയ്യാൻ Encapsulation ഉപയോഗിക്കുന്നു.

# class Student:
#     def __init__(self):
#         self.__marks = 90

#     def get_marks(self):
#         return self.__marks

# s = Student()

# print(s.get_marks())



# Encapsulation എന്ന് പറഞ്ഞാൽ ഒരു class-ന്റെ ഉള്ളിൽ data-യും അതിൽ 
# പ്രവർത്തിക്കുന്ന methods-ഉം ഒരുമിച്ച് വെക്കുകയും, ചില data-കളെ 
# നേരിട്ട് പുറത്തുനിന്ന് access ചെയ്യുന്നത് നിയന്ത്രിക്കുകയും ചെയ്യുന്നതാണ്.

# Simple ആയി
# 👉 Data + Methods = Class
# 👉 Data-യെ protect ചെയ്യുന്നത് = :Encapsulation

# 1️⃣ Properties 
# Property എന്നാൽ class-ന്റെ ഉള്ളിൽ സൂക്ഷിക്കുന്ന data / variable ആണ്.

# class Student:
#     name = "Anu"
#     mark = 90

# name → Property
# mark → Property
# അതായത് student-ന്റെ name, mark എന്നിവയാണ് data/properties.

# 2️⃣ Methods
# Method എന്നാൽ class-ന്റെ ഉള്ളിൽ എഴുതുന്ന function ആണ്.
# ഇത് class-ന്റെ data ഉപയോഗിച്ച് എന്തെങ്കിലും പ്രവർത്തനം ചെയ്യാൻ
#  ഉപയോഗിക്കുന്നു.

# class Student:
#     def display(self):
#         print("Student Details")

# ഇവിടെ display() ആണ് method.

# ഓർക്കാൻ:
# Property = Data
# Method = Work/Action

# 3️⃣ Encapsulation-ലെ Properties-ന്റെ Types
# Python-ൽ properties-നെ access ചെയ്യുന്നതിന്റെ അടിസ്ഥാനത്തിൽ 3 types 
# ആയി പഠിക്കാം.

# 🟢 1. Public Property
# എല്ലായിടത്തുനിന്നും access ചെയ്യാൻ കഴിയുന്ന property.

# name = "Anu"
# ഇവിടെ name public ആണ്.

# 🟡 2. Protected Property
# ഒരു single underscore _ ഉപയോഗിക്കുന്നു.

# _name = "Anu"
# _name protected property ആണ്.

# ഇത് സാധാരണയായി class-ന്റെയും child class-ന്റെയും internal use
#  സൂചിപ്പിക്കാൻ ആണ് ഉപയോഗിക്കുന്നത്.

# 🔴 3. Private Property
# double underscore __ ഉപയോഗിക്കുന്നു.

# __mark = 90
# __mark private property ആണ്.

# ഇത് പുറത്തുനിന്ന് നേരിട്ട് access ചെയ്യുന്നത് തടയാൻ ഉപയോഗിക്കുന്നു.

# 4️⃣ Methods-ന്റെ Types
# Methods-നും ഇതുപോലെ 3 access levels പറയാം.

# 🟢 Public Method

# def display(self):
#     print("Hello")

# s=Student()
# s.dispaly()

# എവിടെനിന്നും call ചെയ്യാൻ സാധിക്കും.

# 🟡 Protected Method

# def _display(self):
#     print("Hello")

# _ ഉപയോഗിക്കുന്നു.
# Internal/subclass use സൂചിപ്പിക്കുന്നു.

# 🔴 Private Method

# def __display(self):
#     print("Hello")

# __ ഉപയോഗിക്കുന്നു.
# Direct access നിയന്ത്രിക്കുന്നു.

# class Student:

#     def display(self):
#         print("Public")

#     def _show(self):
#         print("Protected")

#     def __secret(self):
#         print("Private")

# 5️⃣ Getter Method 
# Private property-യുടെ value വായിക്കാൻ/access ചെയ്യാൻ ഉപയോഗിക്കുന്ന 
# method ആണ് Getter.

# Example:

# def get_mark(self):
#     return self.__mark

# ഇവിടെ get_mark() → Getter method.
# Getter = value എടുക്കാൻ


# 6️⃣ Setter Method 
# Private property-യുടെ value മാറ്റാൻ/update ചെയ്യാൻ ഉപയോഗിക്കുന്ന method
# ആണ് Setter.

# def set_mark(self, mark):
#     self.__mark = mark

# ഇവിടെ set_mark() → Setter method.
# Setter = value മാറ്റാൻ

# Easy ആയി ഓർക്കാൻ:
# GET → എടുക്കുക
# SET → മാറ്റുക

# 7️⃣ Full Example

# class Student:

#     def __init__(self, mark):
#         self.__mark = mark

#     def get_mark(self):
#         return self.__mark

#     def set_mark(self, mark):
#         self.__mark = mark

# student = Student(90)
# print(student.get_mark())
# student.set_mark(95)
# print(student.get_mark())


# Student → Class
# __mark → Private Property
# get_mark() → Getter Method
# set_mark() → Setter Method
# 90 → Initial value
# 95 → Updated value

# ⭐ Encapsulation ?
# പ്രധാനമായും data protection നാണ്.
# അതായത്:
# Data direct access ചെയ്യുന്നത് നിയന്ത്രിക്കാം.
# Data സുരക്ഷിതമായി സൂക്ഷിക്കാം.
# Data മാറ്റുന്നത് control ചെയ്യാം.
# Invalid values തടയാം.
# Code കൂടുതൽ organized ആക്കാം.

# POLYMORPHISM

# class dog:
#     def action(self):
#         print("dog is running")

# class cat:
#     def action(self):
#         print("cat is jumping")

# dog=dog()
# cat=cat()

# dog.action()
# cat.action()

# types
# 1.method overloading
# 2.method overriding
# 3.operator overloaing
# 4.duck typing

# 2.method overriding

# class payment:
#     def pay(self):
#         print("payment")

# class upi(payment):
#     def pay(payment):
#         print("payment using upi")

# class card(payment):
#     def pay(payment):
#         print("payment using card")

# p1=upi()
# p2=card()

# p1.pay()
# p2.pay()

# method overloading

# class Calculator:

#     def add(self, *numbers):
#         return sum(numbers)


# c = Calculator()
# print(c.add(10, 20))
# print(c.add(10, 20, 30))
# print(c.add(10, 20, 30, 40))

# operator overloading

# class Number:
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         return self.value + other.value


# num1 = Number(10)
# num2 = Number(20)

# print(num1 + num2)

# duck typing

# class Car:
#     def start(self):
#         print("Car is starting")


# class Bike:
#     def start(self):
#         print("Bike is starting")


# car = Car()
# bike = Bike()

# def start_vehicle(vehicle):
#     vehicle.start()

# start_vehicle(car)
# start_vehicle(bike)

# data abstration

# from abc import ABC, abstractmethod
# class Payment(ABC):

#     @abstractmethod
#     def pay(self):
#         pass


# class UPI(Payment):

#     def pay(self):
#         print("Payment using UPI")


# payment = UPI()
# payment.pay()