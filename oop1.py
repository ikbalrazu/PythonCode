
class Student:
    #constructor
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def print_row(self):
        print(self.name,self.id)

#stu_name=input("Enter Student Name: ")
#stu_id=input("Enter Student Id: ")
stu_name="iqbal"
stu_id="1703"
show_details=Student(stu_name,stu_id)
show_details.print_row()

class Phone:
    def call(self):
        print("YOU CAN CALL ANYONE")
    def message(self):
        print("You can sent message anyone")

class Samsung(Phone):
    def games(self):
        print("You can play games without any problem")

    def message(self):
        print("You can sent message anyone")



run=Samsung()
run.call()
run.message()
run.games()
print(issubclass(Samsung,Phone))
print("-----------------------------------------------------")
# method overriding

class CellPhone:
    def __init__(self):
        print("This is CellPhone class constructor")

    def feature(self):
        print("You can make call")
        print("You can sent message")
        print("You can access browsing and play online games")
class Iphone(CellPhone):
    #pass
    def __init__(self):
        super().__init__()
        print("This is iphone class constructor")

    def feature(self):
        print("You can make call")
        print("You can sent message")
        print("You can access browsing and play online games")
        super().feature()

check=Iphone()
check.feature()