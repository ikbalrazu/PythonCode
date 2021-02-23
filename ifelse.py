
#for statement 1: if statement
#for statement 2: if statement,else statement
#for statement 3 or more: if statement, elif statement..........., else statement



'''
age=int(input("Enter your age: "))
if(20<=age):
    print("You are adult")
elif(20>age):
    print("You are tenager")
else:
    print("you are not adult")
'''

#inner if or nested if statement
#when many if statement stay into one if statement then called inner or nested if
if 10>8:
    if 12>15:
        print("not true")

    else:
        print("true")

#tarnary operator
print(10 if 10>5 else 50)
'''
def num(n):
    for i in range(n):
        f=i*n+1
        print(f)
num(int(input()))
'''


def runerup():
    n = int(input())
    arr = map(int, input().split())
    print(n)
    print(arr)
runerup()