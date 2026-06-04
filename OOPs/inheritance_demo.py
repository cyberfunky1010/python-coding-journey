class User():
    
    def login(self):
        print("login")

    def register(self):
        print("register")


class Student(User):  #this syntax defines Student is child class of parent class 'User'

    def enroll(self):
        print("enroll")

    def review(self):
        print("review")


s1 = Student()

s1.enroll()
s1.login()
s1.register()
s1.review()

# a child can inherit properties of parent class but not the opposite. here is example
print("***********************")
u = User()

u.login()
u.register()
#but you cannot do
# u.enroll or u.review
