'''
n = int(input("Enter multiplication number: "))

for i in range(10):
    multi = n*(i+1)
    print(f"{n} x {i+1}: {multi}")

'''
'''
def cal(meal_cost,tip_percent,tax_percent):
    tip = (meal_cost / 100) * tip_percent
    tax = (tax_percent / 100) * tip_percent
    total_cost = meal_cost + tip + tax
    print(round(total_cost))
meal_cost=int(input())
tip_percent=int(input())
tax_percent=int(input())
cal(meal_cost,tip_percent,tax_percent)
#tip=(meal_cost/100)*tip_percent
#tax=(tax_percent/100)*tip_percent

#total_cost=meal_cost+tip+tax
#print(round(total_cost))
'''
#string validators
def fun1(s):
    for i in range(len(s)):
        if (s[i].isalnum()):
            return True;
            break;
    return False;

def fun2(s):
    for i in range(len(s)):
        if (s[i].isalpha()):
            return True;
            break;
    return False;

def fun3(s):
    for i in range(len(s)):
        if (s[i].isdigit()):
            return True;
            break;
    return False;

def fun4(s):
    for i in range(len(s)):
        if (s[i].islower()):
            return True;
            break;
    return False;

def fun5(s):
    for i in range(len(s)):
        if (s[i].isupper()):
            return True;
            break;
    return False;

s = input("Enter any string: ")
number = fun1(s)
alpha = fun1(s)
digit = fun1(s)
lowercase = fun1(s)
uppercase = fun1(s)
print(number)
print(alpha)
print(digit)
print(lowercase)
print(uppercase)