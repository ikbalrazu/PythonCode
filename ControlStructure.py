
#if else statement

a=10
b=20
if a!=10:
    print("True")
else:
    print("False")

# if elif

if a>b:
    print("a is powerful")

elif a<b:
    print("b is powerful")

#loop - for, while

value=1
name='iqbal'
while value<=5:
    print(name)
    value = value+1

cold_drinks=['cook','pepsi','7up','merinda']
for drinks in cold_drinks:
    print(drinks)

for mn in range(5,10):
    print(mn)
#list
num=[10,20,30,40,50]
name=['iqbal','raju','arif','safi']
print(num[0],num[3],name[2])

number=10
another_number=[number,20,50]
number_list=[another_number,60,70,90]
print(number_list)
print(number_list[0][2])

messege=['hello world','hello bangladesh','hello there']
messege[0]='a'
print(messege)

fruits=['mango','apple','banana','pineapple']
print('lichu' in fruits)
print('lichu' not in fruits)
print(not 'apple' in fruits)

print(dir(list))
print(help(list.append))

#range
#my_numbers=list(range(10))
#my_numbers=list(range(5,10))
my_numbers=list(range(5,30,3))
print(my_numbers)


