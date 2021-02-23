# logical operators are and or not
num1=40
num2=30
num3=50
if num1<num2 and num2<num3:
    print("Condition is true")
elif num1>num2 and num2>num3:
    print("condition is not true")
else:
    print("Both are not true")

ch=input("Enter Your character: ")
if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
    print("Vowel")
else:
    print("consonant")

#letter grade program
mark=75
if 70<=mark <=80:
    print("A+")
else:
    print("A")