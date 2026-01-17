# asks user as much as wish

a = b = c = 0

ctr = 'y'
while ctr == 'y':
    a = int(input("enter a: "))
    b = int(input("enter b: "))

    if b == 0:
        print("division by zero error !")
        break
    else:
        c = a/b
        print("Quotient = ",c)
        ctr = input("enter (y/n )")
print("program over !!")        

# runs for n number of times (for loop)

x = y = z = 0

for a in range(1,6):

    x = int(input("enter x: "))
    y = int(input("enter y: "))
    if y == 0:
        print("zero by division error !!")
        break
    else:
        z = x/y
        print("quotient: ",z)
print("program over !!")    