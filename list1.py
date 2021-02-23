from pip._vendor.distlib.compat import raw_input

listvalue=[10,20,30,40,'iqbal']

sum = listvalue[0]+listvalue[1]
print(listvalue[0])
print(sum)


#students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
'''
students=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name,score])
print(sorted(students))
'''
print(set([1,2,3]))

subject = ["bangla","english","math","science"]

txt="hello, my name is iqbal"
print(txt.strip(",iq"))
'''
val1 = "Enter your name"
val2 = raw_input(val1)
print(val2)
'''


#get a list as input from user
lis = []
sum = 0
elements = int(input("Enter number of elements: "))

for i in range(elements):
    value = int(input(f"Enter your list value {i}: "))
    lis.append(value)
for n in lis:
    sum +=int(n)
lis.sort()
print(lis)
print(sum)

#get a list as input from user easy way
#s = input("Enter your element: ")
#numbers = list(map(int, s.split()))
#print(numbers)

# nested list

my_list = []
temp_list = []

ele = int(input("Enter size of list: "))
for h in range(ele):
    for g in range(0,2):
        temp_list.append(input())

    my_list.append(temp_list)
    temp_list=[]
print(my_list)

