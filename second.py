# name="mariyam"
# age=21                                  if,else,if else,nested if
# if name:
#     print("i am in if body")
#     if age>25:
#         print("age is > 25")
#     else:
#         print("age is < 25")
# else:
#     print("if else body")


# if,elif_else


# day=int(input("enter a number : "))
# if day==1:
#     print("sunday")
# elif day==2:
#     print("monday")
# elif day==3:
#     print("tuesday")
# elif day==4:
#     print("wednesday")
# elif day==5:
#     print("thursday")
# elif day==6:
#     print("friday")
# elif day==7:
#     print("saturday")
# else:
#     pr
# int("entered number have no day")

# IF

# 1. number=int(input("enter the number : "))
# if number >0:
#     print("positive number")

# 2. marks=int(input("enter marks : "))
# if marks >=50:
#     print("pass")

# 3. age=int(input("enter the age : "))
# if age >=18:
#     print("eligible to vote")

# 4 .number=int(input("enter the number : "))
# if number % 5==0:
#     print("divisible by 5")

# 5. number=int(input("enter the number : "))
# if number>100:
#     print("number is greater than 100")

# IF ELSE

# 1. number=int(input("enter the number : "))
# if number % 2==0:
#     print("even")
# else:
#     print("odd")

# 2. marks=int(input("enter marks : "))
# if marks>=40:
#     print("pass")
# else:
#     print("fail")

# 3. age=int(input("enter age : "))
# if age>=18:
#     print("eligible to vote")
# else:
#     print("not eligibke to vote")

# 4. number=int(input("enter the number : "))
# if number>=0:
#     print("positive")
# else:
#     print("negative")

# 5. amount=int(input("enter the purchase amount : "))
# if amount>5000:
#     print("eligible for discount")
# else:
#     print("not eligible for discount")

# NESTED IF

# age=int(input("enter age : "))
# if age>=18:
#     test=input("driving test completed ?")
#     if test=="yes":
#         print("eligible for driving license")

# 2. attendance=int(input("enter attendance : "))
# if attendance>=75:
#     fee=input("enter fee paid ? ")
#     if fee=="yes":
#         print("eligible for exam")

# 3. age=int(input("enter age : "))
# if age>=21:
#     salary=int(input("enter monthly salary : "))
#     if salary>=25000:
#         print("eligible for loan")

# 4. login=input("are you logged in ? ")
# if login=="yes":
#     balance=int(input("enter balance : "))
#     price=int(input("enter product price : "))
#     if balance>=price:
#         print("can purchase")

# 5. marks=int(input("enter marks : "))
# if marks>=50:
#     exam=input("entrance exam completed ? ")
#     if exam=="yes":
#         print("eligible for college admission")

# IF ELIF ELSE

# 1. marks=int(input("enter marks : "))
# if marks>=90:
#     print("Grade A")
# elif marks>=75:
#     print("Grade B")
# elif marks>=60:
#     print("Grade C")
# elif marks>=40:
#     print("Grade D")
# else:
#     print("Grade F")

# 2.number=int(input("enter a number : "))
# if number>0:
#     print("positive")
# elif number<0:
#     print("negative")
# else:
#     print("zero")

# 3. day=int(input("enter day number : "))
# if day==1:
#     print("sunday")
# elif day==2:
#     print("monday")
# elif day==3:
#     print("tuesday")
# elif day==4:
#     print("wednesday")
# elif day==5:
#     print("thursday")
# elif day==6:
#     print("friday")
# elif day==7:
#     print("saturday")
# else:
#     print("invalid day")

# 4. amount=int(input("enter purchase amount : "))
# if amount>=10000:
#     print("20 % Discount")
# elif amount>=5000:
#     print("10 % Discount")
# elif amount>=2000:
#     print("5 % Discount")
# else:
#     print("no discount")

# 5. age=int(input("enter age : "))
# if age<=12:
#     print("child")
# elif age<=19:
#     print("teenager")
# elif age<=59:
#     print("adult")
# else:
#     print("senior citizen")


# LOOPS

# print(range(10,20))
# print(list(range(5,20,2)))
# print(list(range(20,10,-1)))

# FOR LOOP

# n=5
# for i in range(n):
#     print(i)

# name="mariyam"
# for i in name:
#     print(i,end=" ")

# numbers=[45,26,98,56,46,98,34]
# l=[]
# for i in numbers:
#     if i % 2==0:
#         l.append(i)
# print(l)

# names=["divya","diya","pooja","mariyam"]
# for i in names:
#     for j in i:                                           innerloop
#         print(j,end="")

#     print()


# WHILE LOOP

# n=1
# while n<=10:
#     print(n)
#     n=n+1

# name="mariyam"
# length=len(name)
# i=0
# while i<length:
#     print(name[i])
#     i=i+1

# loop

# 1. for i in range(1,11):
#     print(i)

# 2. for i in range(2,51,2):
#     print(i)

# 3.for i in range(1,51,2):
#     print(i)
   
# 4. sum=0
# for i in range(1,101):
#     sum=sum+i
#     print(i)

# 5. n=int(input("enter a number : "))
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)

# 6. n=int(input("enter a number : "))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print("factorial=",fact)

# 7. count=0
# for i in range(1,101):
#     if i % 3==0:
#         count=count+1
# print(count)

# 8. for i in range(10,0,-1):
#     print(i)

# 9. sum=0
# for i in range(2,101,2):
#     sum=sum+i
# print(sum)

# 10. for i in range(1,11):
#     print(i*i)

# while Loop

# 1. i=1
# while i <=10:
#     print(i)
#     i=i+1

# 2. i=2
# while i <= 50:
#     print(i)
#     i=i+2

# 3. i=1
# sum=0
# while i <= 100:
#     sum=sum+i
#     i=i+1
# print(sum)

# 4. n=int(input("enter a number : "))
# i=1
# while i <= 10:
#     print(n,"*",i,"=",n*i)
#     i=i+1

# 5. n=int(input("enter a number : "))
# fact=1
# i=1
# while i <= n:
#     fact=fact*i
#     i=i+1
# print("factorial =",fact)

# 6. i=20
# while i >= 1:
#     print(i)
#     i=i-1

# 7. n=int(input("enter a number : "))
# count=0
# while n > 0:
#     count=count+1
#     n=n//10
# print("number of digits =",count)

# 8. n=int(input("enter a number : "))
# sum=0
# while n >0:
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# print("sum=",sum)

# 9. n=int(input("enter a number :"))
# reverse=0
# while n >0:
#     digit=n%10
#     reverse=reverse*10+digit
#     n=n//10
# print("reverse=",reverse)

# 10. sum=0
# n=int(input("enter a number : "))
# while n !=0:
#     sum=sum+n
#     n=int(input("enter a number : "))
# print("sum=",sum)

# list comprehension

# numbers=[1,2,3,4,5]
# a=[x for x in numbers]
# print(a)


# l=[i for i in range(11) if i % 2==0]
# print(l)


# function

# def add():
#     print(5+3)


# def name():
#     print("mariyam")

# add()
# name()

# ((4 types of functions are:)

# 1. with argument with return
# 2. with argument without return
# 3. without argument with return
# 4. without argument without return)

# 1 .with argument with return

# def add(a,b):
#     return a+b
# print(add(5,3))

# 2. with argument without return

# def add(a,b):
#     print(a+b)
# add(5,3)

# 3. without argument with return 

# def add():
#     return 5+3
# print(add())

# 4. without argument without return

# def add():
#     print(5+3)
# add()


# def number_add(a,b):
#     return a+b


# p=int(input("enter your first number : "))
# s=int(input("enter your second number : "))

# answer=number_add(p,s)
# print("answer=",answer)


# n=int(input("enter a number : "))
# if n==0:
#     print("n is 0")
# else:
#     print("n is not 0")