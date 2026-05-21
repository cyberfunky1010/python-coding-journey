class Atm:
    
    #constructor
    def __init__(self):
        self.__pin = ""       # __ strong convention for internal use. this becommes _Atm__pin and still can be accessed 
        self.__balance = 0                                        #and this becomes _Atm__balance and still can be accessed 
            
    def get(self):                 # a getter. here it is used to get pin
        print(self.__pin)

    def set(self):        # a setter. here it used to change or update pin according to my defined rule. so it must be in control. 
        new_pin = input('set new pin: ')

        if new_pin.isdigit():
            self.__pin = new_pin
            print("pin changed succssfully")
        else:
            print("not allowed")   

    def menu(self):

        while True:   
            user_input = input(""" 
                       \t hello, how would you like to proced
                            1. Enter 1 to create pin
                            2. Enter 2 to deposit 
                            3. Enter 3 to withdrawl
                            4. Enter 4 to check balance
                            5. Enter 5 to change pin
                            6. enter 6 to get pin
                            7. enter 7 to set pin
                            8. press any key to exit   
             """)
            if user_input == '1':
                self.set_pin()

            elif user_input == '2':
                self.deposit()    
        
            elif user_input == '3':
                self.withdrawl()

            elif user_input == '4':
                self.check_balance()

            elif user_input == '5':
                self.change_pin()

            elif user_input == '6':
                self.get()

            elif user_input == '7':
                self.set()
            
            else: 
                self.quit_program()
                break  
     
    def set_pin(self):
        print(f" \t SET PIN MENU")
        if not self.__pin:
            self.__pin = input('create a PIN: ')
            print("PIN created successfully !!!")
        else:
            print("pin already created")

    def change_pin(self):
        print(f" \t PIN CHANGE MENU")
        if self.__pin:
            temp = input("enter pin:")
            if temp == self.__pin:
                 self.__pin = input("new pin: ")
                 print("PIN changed successfully")
            else:
                print("wrong PIN entered. try again")     
        else:
            print("no pin set. try creating one")

    def deposit(self):
        print(f" \t MONEY DEPOSIT MENU")
        if self.__pin:
            
            temp = input(f'enter pin: ')
            if temp == self.__pin:
                amount = int(input(f'enter amount: '))
                self.__balance = self.__balance + amount     
            else:
                print(f'WRONG PIN. try again')    
        else:
            print('pin not set')

    def withdrawl(self):
        print(f" \t MONEY WITHDRAWL MENU")
        if self.__pin:
            temp = input(f'enter pin: ')
            if temp == self.__pin:
                amount = int(input(f'enter amount: '))
                if amount <= self.__balance:
                    self.__balance = self.__balance - amount
                else:
                    print('insufficient funds')
                    print(f'try less than {self.__balance}')
            else:
                print(f'WRONG PIN. try again')
        else:
            print("pin not set")

    def check_balance(self):
        print(f" \t CHECK BALANCE MENU")
        if self.__pin:
            temp = input('enter pin: ')
            if temp == self.__pin:
                print(self.__balance)
            else:
                print('invalid PIN !!!')
        else:
            print("pin not set")

    def quit_program(self):
        print('exit !!!')      
               

# here you can make as much object as you want.
# can also create objects on python shell. 

# you can also directly access the constructor varible by obj.balance >> 0  or you can see pin by sbi.pin 
# to hide it you do

sbi = Atm()        # object or instance created
sbi.menu()

