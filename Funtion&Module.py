from itertools import count

# function

def sum(x,y):
    c=x+y
    print("The sum is",c)

sumvalue=sum(10,20)

def add_explanation(line):
    return line + '!'

update_line = add_explanation

print(update_line("Hello World"))

def beautify(text):
    return text+'!!!'
def make_line(func,words):
    return "Hello "+func(words)
print(make_line(beautify,"world"))

def make_double(x):
    return x*2

my_marks=[10,20,30,40,50]
#map(function,list)
result=map(make_double,my_marks)
print(list(result))

#filter
def is_even(x):
    return x%2 == 0

my_numbers=[1,2,3,4,5,6]
even_result=filter(is_even,my_numbers)
print(list(even_result))

#genarator
def my_iterable():
    i=5
    while i>0:
        yield i
        i -=1

for i in my_iterable():
    print(i)

#decorator
def my_decorator(func):
    def decorate():
        print("------------------")
        func()
        print("------------------")
    return decorate


def printsome():
    print("Hello world")

decorated_function=my_decorator(printsome)
decorated_function()

#another example of decorator

def my_decorator1(func):
    def decorate():
        print("------------------------")
        func()
        print("-------------------------")
    return decorate

@my_decorator1
def print_raw():
    print("My name is iqbal")
print_raw()

#itertools
for i in count(5):
    print(i)
    if i>=11:
        break

#xxargs
def student(*details):
    print(details)

result=student(1703,"iqbal")

#xxxargs
def teacher(**details):
    print(details)
teacher_result=teacher(id=1703,name='iqbal')