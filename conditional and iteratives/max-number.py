x = int(input("enter x: "))
y = int(input("enter y: "))
z = int(input("enter z: "))

if x > y and x > z:
    print(x,"is the greatest")

elif y > x and y > z:
    print(y,"is the greatest")

elif z > x and z > y:
    print(z,"is the greatest")