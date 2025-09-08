x = y = z = 0

x = int(input("enter x: "))
y = int(input("enter y: "))
z = int(input("enter z: "))

max = x
if y > max:
    max = y

if z > max:
    max = z    

print("largest number is", max)    