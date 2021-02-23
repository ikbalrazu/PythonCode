"""
def function(num1,num2):
    sum=num1+num2
    print(sum)
def function2():
    print("i am a function")
function(20,24)
function2()
"""

#default global and local variables
var=10
def myfunction(name,age=22):  #default variables
    print(name,age)
def globalvar():
    loc=var
    loc=loc+10
    print(loc)
myfunction("iqbal",30)
globalvar()


