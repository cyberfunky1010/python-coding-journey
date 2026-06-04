class Atm():

    __counter = 1  # static / class variable is always created outside constructor. right way to access 'counter' Atm.counter and not obj.counter
                            #when you access instance var you use self but in static you use class like Atm.counter
    def __init__(self):
         # instance variable
        self.__pin = ""
        self.__balance = 0
    
        self.sno = Atm.__counter
        Atm.__counter = Atm.__counter + 1
         
        # self.menu()  #its not a good idea that menu() is here in constructor. it should down the last

    @staticmethod   #to show it is a static method. in this we don't need self. everything is accessed via class directly. 
    def get_counter():        # don't need 'self' here cuz it deals with static variable 
        return Atm.__counter 
     
    @staticmethod 
    def set_counter(new):
         if type(new) == int:
            Atm.__counter = new
         else:
              print("not allowed")
 
    def menu(self):            

            user_input = input(f"""

                     \t  hello how would you like to proceed?

                         1. to create pin
                         2. to deposit             
                         3. to withdraw
                         4. to check balance  
                            press any key to exit             
""")  
            
            if user_input == '1':
                 self.create_pin()
            elif user_input == '2':
                 self.deposit()
            elif user_input == '3':
                 self.withdrawl()
            elif user_input == '4':
                 self.check_balance()
            else:
                 self.quit()            
            
    def create_pin(self):
         self.__pin = input("enter pin: ")
         print("pin created successfully !!!")

         self.menu()

    def  deposit(self):
         temp = input(f"enter pin")
         if temp == self.__pin:
              amt = int(input("enter amount: "))
              self.__balance = self.__balance + amt
              print(f"deposited amount")
         else: 
              print(f"wrong pin entered")     
    
         self.menu()

    def withdrawl(self):
        temp = input("enter pin: ")
        if temp == self.__pin:
             amt = int(input("enter amount: "))
             self.__balance = self.__balance - amt
             print(f"withdrawn successfull !!!")

        else:
             print(f"wrong pin entered!!! ")     
        self.menu()
    def check_balance(self):
         temp = input("enter pin: ")
         if temp == self.__pin:
              print(f"{self.__balance}")
         else:
              print(f"wrong pin entered")     
         self.menu()
    def quit(self):
         print("program exit !!!")         



   