class Customer():

    def __init__(self, name):

        self.name = name

def greet(customer):
    print(id(customer))

    customer.name = 'muhammad'
    print(customer.name)
    print(id(customer)) # same address as cust. means you are able to edit it same address. means it is mutable.
    # this shows class objects are also mutable like lists, dict and sets

cust = Customer('aquib') #'cust' is reference variable

greet(cust)              # sending reference variable are argument

print(id(cust))
print(cust.name)

#cust and customer are aliases. 
# greet the object 'name' so it is a mutable data type. 
# when are able to edit on same address that means it is mutable.

print("*******************************************************")
def change(L):
    print(id(L))
    L.append(5)
    print(L)
    print(id(L))

L1 = [1,2,3]

print(id(L1))
print(L1)
change(L1[:]) # cloning it so that the orginal list doesn't modify. doing this the list inside function is modified and has different address but original list remains.
print(L1)     # this shows its risky if you send lists (including objects) in function calling buz it could modify.
              # SOLUTION: clone it : change(L1[:])
              # but if you were sending tuple then it doesn't matter cuz it is non-mutable.