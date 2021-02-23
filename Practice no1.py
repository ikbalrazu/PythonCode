import random
#indentation is very important in python

#variable
"""
name="iqbal"
old=23
var3=5.56
#output
print("My name is",name)
print("And i am",old,"years old")
"""
#random numbers
#print(random.randrange(1,10))

#input and type casting
"""
First_Value=int(input("Enter Your First Value: "))
Last_Value=int(input("Enter Your Last Value: "))

sum=First_Value+Last_Value

print("The sum is",sum)
"""
#string
"""
var="Hello World!"
print(len(var))
print(var[6])
print(var.lower())
print(var.upper())
"""
#Operators
"""
Arithmetic operators  + - * / % **(2**3)=2*2*2
Assignment operators  += -= *= /= **= //=
Comparison operators  == != > < >= <=
Logical operators     and or not
Identity operators    is , is not
Membership operators  in , not in
Bitwise operators   & |
"""
#List
"""
Subject=["Bangla","English","Math","Science"]
for x in Subject:
    print(x)

Subject.append("ICT")
Subject.reverse()
print(Subject)
"""
"""
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
"""
#set
"""
thisset={"apple","banana","orange"}
for x in thisset:
    print(x)
thisset.add("orange")
print("banana" in thisset)
"""
#if-else
"""
age=int(input("Enter Your age: "))
if age<18:
    print("You are under 18. Not allow")
elif age>18:
    print("You are adult. You are allow")
elif age==18:
    print("You are 18 years old. Plz contact with manager")
else:
    print("Your age are not meet with condition")

"""
#While LOOP
"""
a=1
while a<=10:
    print("Md ikbal hossen raju")
    a=a+1
"""
#function or method in python
def fun_one(name):
    print("MD "+name)

fun_one("iqbal")
fun_one("Raju")
fun_one("Karim")
fun_one("Rahim")