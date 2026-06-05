############################ inheriting Constructor #######################

class Phone:

    def __init__(self, price, brand, camera):
         print("inside Phone constructor")       
         self.price = price
         self.brand = brand
         self.camera = camera


class SmartPhone(Phone):
     pass                             # if child class has no constructor then parent class constructor is called. 

s = SmartPhone(21000, "Samsung", "laika")

print(s.brand)


############################ Eg2 - inheriting Private members #############
print("****************************************************")

class Phone:

    def __init__(self, price, brand, camera):
         print("inside Phone constructor")
         self.price = price
         self.__brand = brand   # Private member - child class cannot access if try to then code crashes.
         self.camera = camera


class SmartPhone(Phone):
     pass

s = SmartPhone(21000, "Samsung", "laika")

# print(s.__brand)       # since brance is private data member, you can't access it doing so results in code crash. ERROR CODE: SmartPhone' object has no attribute 'brand'

########################## Eg3 - Polymorphism ###############################
print("***************************************************")

class Phone:

    def __init__(self, price, brand, camera):
         print("inside Phone constructor")       
         self.price = price
         self.brand = brand
         self.camera = camera

    def buy(self):
         print("buying Phone")

class SmartPhone(Phone):
     
     def buy(self):
          print("buying Smart Phone")          

s = SmartPhone(21000, "Samsung", "laika")

s.buy()  #here SmartPhone's object is calling buy. since 'buy' exist in both classes, SmartPhone's 'buy' will override parent class. hence 'buying smart phone' will be printed.

########################## example class parent 1 ############################ 
print("*************************************************")

class Parent:
     
     def __init__(self, num):
          self.__num = num

     def get_num(self):
          return self.__num

class Child(Parent):
     
     def show(self):
          print("inside child class")

son = Child(250)
print(son.get_num())
son.show()

########################## Example 2 ###########################################
print("**************************************************")

class Parent:
     
     def __init__(self, num):
          self.__num = num

     def get_num(self):
          return self.__num

class Child(Parent):
     
     def __init__(self, val, num):   # here val = 100 but doesn't defined num what i've to do with this, no code written for this.
          self.val = val
 
     def show(self):
          print("inside child class")      # program flow
                                           # invoked child class and it has constructor so parent constructor will not be called and no value wiil be assigned.      
son = Child(100, 25)
# print(son.get_num())                       # this result in error cuz parent class was never invoked since no object was created. it would have automatically triggered
                                           # if child class had no constructor. if however child class had no constructor then 100 would have printed. 

######################### Example 3 #########################################
print("*****************************************************")

class A:
     
     def __init__(self):
          self.var1 = 100                 #here self.var1 is hard coded so whenever we use self.var1 always 100 will be printed. 

     def display1(self, var1):
         print(f"class A: {self.var1}")   #here you'r using self, its class attribute so 100 will be printing.
         print(f"class A: {var1}")        #here actually you'r using the variable var1 so 250 will be printed.

class B(A):
     
     def display2(self, var1):
          print(f"class B: {self.var1}")
          print(f"class B: {var1}")

obj = B()
obj.display1(250)   
obj.display2(400)       

####################### Example of Super ###############################
print("****************************************************")

class Phone:

    def __init__(self, price, brand, camera):
         print("inside Phone constructor")       
         self.price = price
         self.brand = brand
         self.camera = camera

    def buy(self):
         print("buying Phone")

class SmartPhone(Phone):
     
     def buy(self):
          print("buying Smart Phone")   
          super().buy()  # here control reaches to parent class       

s = SmartPhone(21000, "Samsung", "laika")

s.buy()

#you cannot do this - s.super().buy() - cannot use super() outside class.

######################## Super example with constructor ################### here you understand actualy utility of super ######
print("************************************************") 

class Phone:
     
     def __init__(self, price, brand, camera):
          print("inside Phone constructor")
          self.__price = price
          self.brand = brand
          self.camera = camera
    
     def get_price(self):
          return self.__price

class SmartPhone(Phone):

     def __init__(self, price, brand, camera, os, ram):
          print("first here")
          super().__init__(price, brand, camera)
          self.os = os
          self.ram = ram
          print("inside SmartPhone")

s = SmartPhone(25000, "Samsung", "laika", "android", 8)

print(s.brand, s.camera, s.os, s.ram)
print(s.get_price())

####################### Example 1 of Super ################################
print("*************************************************")

class Parent:
     
     def __init__(self, num):
          
          self.__num = num

     def get_num(self):
          return self.__num

class Child(Parent):
     
     def __init__(self, var, num):
          
          super().__init__(num)   #using super() to call constructor should be first statement.
          self.__var = var

     def get_var(self):
          return self.__var

obj = Child(200, 100)
print(f"get num {obj.get_num()}")          
print(f"get var {obj.get_var()}")          

####################### Example 2 on Super ###################################
print("*****************************************************")

class Parent:
     
     def __init__(self):
          
          self.num = 100

class Child(Parent):
     
     def __init__(self):
          super().__init__()
          self.var = 200

     def show(self): 
          print(self.var)    
          print(self.num)  # will this work? kya child class ke andar se self ko use krke parents ke attribute ko call kr skte h ya nhi? ans - yes 
                           # because self is the 'son' object and if this object can access from out side then it can access from inside too.  

son = Child()
son.show()      # here when calling show() the 'son' goes to parameter of show() (i.e. self) function. 
               
####################### Example 3 on Super ###################################
print("*****************************************************")

class Parent:
     
     def __init__(self):
          
          self.__num = 100
  
     def show(self):                                  # this code doesn't run when object calling son.show() cuz of method overriding.
          print(f"Parent: {self.__num}")

class Child:

     def __init__(self):
           super().__init__()

           self.__var = 20

     def show(self):                                  # this code overrides the parent class show() method cuz of method overriding.
          print(f"Child: {self.__var}")

dad = Parent()
dad.show()

son = Child()
son.show()


####################### Example on Multi-level inheritance ###################################
print("*****************************************************")

class Product:

     def review(self):
          print("product customer review")

class Phone(Product):

     def __init__(self, price ,brand, camera):          
          print("inside Phone constructor")
          
          self.price = price
          self.brand = brand
          self.camera = camera

     def buy(self):
          print("buying a phone")

class SmartPhone(Phone):
     pass

s = SmartPhone(21000, "nokia", "laika")
p = Phone(16000, "redmi", "sony")

s.buy()
s.review()
p.review()

####################### Hierarchical inheritance ########## one parent multiple children #########################
print("*****************************************************")

class Phone:

     def __init__(self, price, brand, camera):

          self.price = price
          self.brand = brand
          self.camera = camera

     def buy(self):
          print("buying a phone")

     def return_phone(self):
          print("returning a phone")     

class SmartPhone(Phone):
     pass

class Feature(SmartPhone):
     pass

# any object of SmartPhone aur Feature can access methods of its parent class Phone.

SmartPhone(24000, "oneplus", "Fujifilm").return_phone()
Feature(12000, "redmi", "nicon").buy()

####################### Multiple inheritance ###################################
print("*****************************************************")

class Phone:

     def __init__(self, price, brand, camera):

          self.price = price
          self.brand = brand
          self.camera = camera

     def buy(self):
          print("buying a phone")

     def return_phone(self):
          print("returning a phone")     

class Product:

     def review(self):
          print("Customer review")

class SmartPhone(Phone, Product): # inheriting from two classes
     pass

s = SmartPhone(15000, "nokia", "laika")

s.buy()
s.review()

####################### method resolution order (MRO) ###################################
print("*****************************************************")

class Phone:

     def __init__(self, price, brand, camera):

          self.price = price
          self.brand = brand
          self.camera = camera

     def buy(self):
          print("buying a phone")     

class Product:

     def buy(self):
          print("buying a product")

class SmartPhone(Phone, Product): # According to MRO, when multiple parent classes contain a method with the same name,  
     pass                         # Python executes the method from the class that appears first in the inheritance list.

s = SmartPhone(15000, "xiome", 12)

s.buy() # here phone method will execute cuz of MRO

####################### example 1 on types ###################################
print("*****************************************************")

class A:

     def m1(self):
          return 10
     
class B(A):

     def m1(self):
          return 20

     def m2(self):
          return 30

class C(B):

     def m2(self):
          return 40

obj1 = A()
obj2 = B()
obj3 = C()

print(obj1.m1() + obj3.m1() + obj3.m2()) #here in obj3.m1() there are 2 choices classB or A method to choose 
# 10 + 20 + 40                            logically father's method will run. 

####################### example 2 on types ############################## 
print("*****************************************************")

class A:

     def m1(self):
          return 20
     
class B(A):

     def m1(self):
          val = super().m1() + 30

class C(B):

     def m1(self):
          val = self.m1() + 20 # recustion. here self is the current object so self.m1() = obj.m1(). when this line runs again you call the same method m1() infinitely
          return val           # so after running infinitely python returns "maximum recursion depth exceeded" 
     
# obj = C()       # The work that obj performs outside the class is performed by self inside the class.
# print(obj.m1())

####################### Method overloading ############ 
print("*****************************************************")

class Geometry:                        # technially method overloading doesn't work in python. this program is written with some trick to implement the concept.

     def area(self, a,b =0):
         if b == 0:
              print(f"circle {3.14 * a * a} ")
         else:
              print(f"rectangle {a * b}")

obj = Geometry()

obj.area(4)
obj.area(4,3)