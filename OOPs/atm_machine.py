class Atm:
    
    #constructor
    def __init__(self):
        self.pin = ""
        self.balance = 0
        
        self.menu()

    def menu(self):
        user_input = input(""" 
                   \t hello, how would you like to proced
                        1. Enter 1 to create pin
                        2. Enter 2 to deposit 
                        3. Enter 3 to withdrawl
                        4. Enter 4 to check balance
                        5. Enter 5 to change pin
""")
        if user_input == '1':
            self.set_pin()

        elif user_input == '2':
            self.deposit()    
        
        elif user_input == '3':
            self.withdrawl()

        elif user_input == '4':
            self.check_balance()

        else: 
            print('exit')        
     
    def set_pin(self):
        print(f" \t SET PIN MENU")
        if not self.pin:
            self.pin = input('create a PIN: ')
            print("PIN created successfully !!!")
        else:
            print("pin already created")
    def change_pin(self):
        print(f" \t PIN CHANGE MENU")
        if self.pin:
            temp = input("enter pin:")
            if temp == self.pin:
                 self.pin = input("new pin: ")
                 print("PIN changed successfully")
            else:
                print("wrong PIN entered. try again")     
        else:
            print("no pin set. try creating one")
    def deposit(self):
        print(f" \t MONEY DEPOSIT MENU")
        if self.pin:
            
            temp = input(f'enter pin: ')
            if temp == self.pin:
                amount = int(input(f'enter amount: '))
                self.balance = self.balance + amount     
            else:
                print(f'WRONG PIN. try again')    
        else:
            print('pin not set')
    def withdrawl(self):
        print(f" \t MONEY WITHDRAWL MENU")
        if self.pin:
            temp = input(f'enter pin: ')
            if temp == self.pin:
                amount = int(input(f'enter amount: '))
                if amount < self.balance:
                    self.balance = self.balance - amount
                else:
                    print('insufficient funds')
                    print(f'try less than {self.balance}')
            else:
                print(f'WRONG PIN. try again')
        else:
            print("pin not set")
          
    def check_balance(self):
        print(f" \t CHECK BALANCE MENU")
        if self.pin:
            temp = input('enter pin: ')
            if temp == self.pin:
                print(self.balance)
            else:
                print('invalid PIN !!!')
        else:
            print("pin not set")
    def exit(self):
        print('exit !!!')              

# here you can make as much object as you want.
# can also create objects on python shell. 

sbi = Atm()
