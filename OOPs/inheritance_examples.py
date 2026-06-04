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


               
