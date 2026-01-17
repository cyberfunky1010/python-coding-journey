# find the greatest number.

x = y = z = 0

x = int(input("enter x: "))
y = int(input("enter y: "))
z = int(input("enter z: "))

largest = x   # don't use max here. python will treat it as varible and won't treat it a function for the second part.
if y > largest:
    largest = y

if z > largest:
    largest = z    

print("largest number is", largest)    

# or you can simply do this.

a = int(input("enter a: "))
b = int(input("enter b: "))
c = int(input("enter c: "))

print("largest num : ",max(a,b,c))