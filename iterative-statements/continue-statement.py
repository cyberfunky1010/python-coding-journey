#program to illustrate continue statement using while loop. here we can ask to give answer an many times as we want.

ctr = 'y'

while ctr == 'y':
    a = int(input("enter a: "))
    b = int(input("enter b: "))

    if b == 0:
        print("denominator cannot be zero. enter again")
        continue
    else:
        c = a/b
        print("Quotient: ",c)
        ctr = input("enter again y/n: ")
print("program over!!!")    

#same program using for loop. here we can only ask to give answer for a certain number of times.

for r in range(1,6):
    x = int(input("enter x: "))
    y = int(input("enter y: "))

    if y == 0:
        print("denominator cannot be zero. enter again")
        continue
    else:
        z = x/y
        print("quotient is ", z)
print("program over!!!")        