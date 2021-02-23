
class LoginPage:
    def __init__(self,email,password):
        self.email=email
        self.password=password

    def check(self):
        inputemail=input("Enter your email: ")
        inputpass=input("Enter your password: ")
        if self.email==inputemail and self.password==inputpass:
            print("Login Successful")
        elif self.email==inputemail and self.password!=inputpass:
            print("Login is not successful, password incorrect")
        elif self.email!=inputemail and self.password==inputpass:
            print("Login is not successful, Email incorrect")
        elif self.email!=inputemail and self.password!=inputpass:
            print("Login is not successful, incorrect Email and Password")

login=LoginPage("iqbalraju123@gmail.com","123")
login.check()
