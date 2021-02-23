
value = (20,30,40,50,'iqbal')
print(value)
print(type(value))
print(hash(value))
'''
ele = input("Input some comma separete numbers: ")
list = ele.split(",")
tuplevalue = tuple(list)
print(list)
print(tuplevalue)
print(hash(tuplevalue))
'''

'''
n = int(input("enter tuple number: "))
integer_list = map(int, input().split())
print(integer_list)
'''

value = "this is a string"

make_list =value.split()
make_join ="-".join(make_list)
print(make_list)
print(make_join)


s = input()
print(s.isalnum())
print(s.isalpha())
print(s.isdigit())
print(s.islower())
print(s.isupper())

