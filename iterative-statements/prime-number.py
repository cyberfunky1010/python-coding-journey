num = int(input("enter a number: "))

for a in range(1,num+1):
    if num % a == 0 and num / a == num:
        print("prime number")
        break
else:
    print("not prime")    