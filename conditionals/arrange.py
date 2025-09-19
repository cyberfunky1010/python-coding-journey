# program that reads 3 numbers (interger) and prints them in ascending order.

x = int(input("enter x: "))
y = int(input("enter y: "))
z = int(input("enter y: "))

min = mid = max = None

if y < x and y < z:
     if z > x:
          min, mid, max = y,x,z
     else:
          min, mid, max = y,z,x

elif x < y and x < z:
     if z > y:
          min, mid, max = x, y, z
     else:
          min, mid, max = x, z, y     

else:
       if x > y:
            min, mid, max = z, y, x
       else:
             min, mid, max = z, x, y

print("numbers in ascending order are: ", min,mid,max)             