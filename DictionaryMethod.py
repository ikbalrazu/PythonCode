'''
def switch():
    value1=int(input("Enter your first value: "))
    value2=int(input("Enter your second value: "))
    print("Press 1 for addition \n Press 2 for substraction \n Press 3 for multiplication \n Press 4 for Devision")

    option=int(input("Enter your choice: "))
    def add():
        result=value1+value2
        print(result)
    def sub():
        result=value1-value2
        print(result)
    def mul():
        result=value1*value2
        print(result)
    def div():
        result=value1/value2
        print(result)
    dictionary={
        1:add,
        2:sub,
        3:mul,
        4:div
    }
    dictionary.get(option)()

switch()
'''
thisdict = {
    "brand": "Ford",
    "model": "y25",
    "year": 1964,
    "color": ["balck","blue","red","white"]
}
thisdict["weight"]=500
print(thisdict["model"])
print(thisdict["brand"])
x=thisdict["color"]
y=thisdict.get("year")
z=thisdict.keys()
thisdict.update({"model":"100cc"})
thisdict.update({"color":["black","yewllo","red","brown"]})
thisdict.pop("model")
del thisdict["weight"]
print(x)
print(y)
print(z)
print(thisdict)

student={
    "name":"iqbal",
    "id":1703,
    "department":"swe"

}

print(student)
for i in student:
    print(student[i])

#nested dictionary
myfamily = {
    "child1":{
        "name":"iqbal",
        "age":25
    },
    "child2":{
        "name":"riaz",
        "age":23
    },
    "child3":{
        "name":"fatema",
        "age":17
    }
}

print(myfamily)

dictionary = {
    "thisdict":thisdict,
    "student":student,
    "myfamily":myfamily
}

print(dictionary)