#To inherit a class, you simply incorporate the definition of one class into another

"""
class Father():
    def property(self):
        print("MD IKBAL HOSSEN RAJU")

class Mother():
    def bank_balance(self):
        print("2 crore")

class Child(Father,Mother):
    def access(self):
        print("car home hotel money")


obj=Child()
obj.property()
obj.access()
obj.bank_balance()

"""

class Teacher():
    def details(self,name,id,subject,email):
        self.name=name
        self.id=id
        self.email=email
        self.subject=subject
        print("")


class Department():
    def department_info(self,name,id,teacher):
        self.name=name
        self.id=id
        self.teacher=teacher
        print("")


class Student():
    def stu_info(self,name,id, department):
        self.name=name
        self.id=id
        self.department=department
        print("")




