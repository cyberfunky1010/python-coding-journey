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

# program to illustrate the difference between break and continue

print("the loop with 'break' produces output as: ")

for i in range(1,11):
     if i % 3 == 0:
         break
     else:
         print(i)

print("the loop with 'continue' produces output as: ")

for j in range(1,11):
    if j % 3 == 0:
        continue
    else:
        print(j)