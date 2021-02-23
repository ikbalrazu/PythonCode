class Student:
    stu_name = ""
    stu_id = ""

    def setValue(self,stu_name,stu_id):
        self.stu_name=stu_name
        self.stu_id=stu_id

    def display(self):
        print(f"Student Name: {self.stu_name} and Student id: {self.stu_id}")



iqbal = Student()
name = "iqbal"
id = 1703
iqbal.setValue(name,id)
iqbal.display()

#inheritance
class Animal:
    def ani_head(self):
        print("This is animal class")

    def sameattri(self):
        print("this is animal attrubute")
class University:
    def display(self):
        print("this is university class")
class Person(Animal,University):
    def per_head(self):
        print("nose,hair,ear,eye")

    def per_hand(self):
        print("left hand, right hand")

    def per_leg(self):
        print("left leg, right leg")

    def sameattri(self):
        print("this is person attribute")


call = Person()
call.ani_head()
call.per_head()
call.sameattri()
call.display()

# a practical inheritance example

class Shape:
    def __init__(self,dim1,dim2):
        self.dim1=dim1
        self.dim2=dim2

    def area(self):
        print("This is shape area")

class Traingle(Shape):
    def area(self):
        area = 0.5*self.dim1*self.dim2
        print("Area of traingle: ",area)

class Rectangle(Shape):
    def area(self):
        area = self.dim1*self.dim2
        print("Area of rectangle: ",area)

t1=Traingle(5,10)
t1.area()




