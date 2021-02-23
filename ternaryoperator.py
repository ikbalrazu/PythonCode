num1=int(input("Enter Num1: "))
num2=int(input("Enter Num2: "))

'''

if num2>num1:
    print("num2")
else:
    print("num1")
'''
#print(num1 if num1>num2 else num2)
max=num1 if num1>num2 else num2
print("Maximum value= ",max)