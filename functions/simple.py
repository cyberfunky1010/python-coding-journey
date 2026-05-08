def greet():
    print(f"whatever goes up always \ncomes down")
    print(f" \t\t ~me ")

def square(a):
    return a*a

def sumof3multiples(n):
    s = n*1 + n*2 + n*3
    print(s)
  

greet()
print(square(2))   #here print is must cuz in funciton there is only return statement unlike in funciton sumof3multiple which has already print statement. 
sumof3multiples(2)