#program to demonstrate exception handling.

try:
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    
    if b == 0:
        print("division by zero error !!!")
    else:
        c = a / b
        print(" a / b is ", c)
except:
    print("can only accept integer values")            
