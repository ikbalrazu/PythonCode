
#dictionary
#dictionary with list
#my_marks={"bangla":85,"english":68,"math":98}
my_marks={"Bangla":[20,30,40,50],"English":[50,60,70,80],"Math":[98,56,45,72],"Science":[96,85,45,66]}

print(my_marks["Bangla"],"OR",my_marks["English"])

#dictionary function
no_list={1:1,2:2,3:4,4:"what"}
no_list[4]=5
print(no_list)

#search the key from the dictionary
num={1:"one",2:"two",3:"three",4:"four",5:"five"}
print(1 in num)
print("two" in num)
print(3 in num)
print("five" in num)

print(num.get(6))
print(num.get(6,"6 is not available"))

#tuples
roles=("bangla","english","math","science")
print(roles[1])

permissions = (("Admin", "Operator", "Customer"), ("Developer", "Tester"), [1, 2, 3], {"Stage": "Development"})

print(permissions[3]["Stage"])

numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)

a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)
