#magic method print(dir(int))

class newclass():
    def __init__(self,name,id,department):
        self.name=name
        self.id=id
        self.department=department
        print("My name is",name," My id is ",id,"And my department is",department)

    def print_row(self):
        print("Hello world")

result = newclass("Iqbal","162-35-1703","Software Engineering")
result.print_row()

class Student():
    name = "iqbal hossen"
    id = "162-35-1703"
    department="Software Engineering"
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def details(self,name,id):
        print("My name is",name,"my id is ",id)





