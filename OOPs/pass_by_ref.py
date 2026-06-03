class Customer:

    def __init__(self, name,gender):

        self.name = name
        self.gender = gender

def greet(customer):        # 'customer' receives 'cust' object reference. customer = cust. therefore cust.name = customer.name | customer has 2 things name & gender
    if customer.gender == 'male':
        print(f"hello, {customer.name} sir")    #since customer = cust. cust.name also works
    else: 
        print(f"hello, {customer.name} ma'am")

    cust1 = Customer('muhammad', 'male')  
    return cust1   # a function can also return objects

cust = Customer('aquib', 'male')  # cust holds object reference

new_obj = greet(cust)  #storing value return of 'greet' function # passing class object 'cust' as argument to 'greet' function. usually we do is numbers, strings, lists.  
# cust1 is object of class Customer(). so it returned and stored in new_obj. so new_obj = cust1. 
print(new_obj.name)

#cust and customer are behaving like aliases. both have same id. 