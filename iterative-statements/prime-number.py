# prime number example 

num = int(input("enter a number: "))
lim = int(num/2) + 1    # for efficientcy. only checks number till half of the num.
for i in range(2,lim):
  
    rem = num % i
    if rem == 0:
        print(num,"is not prime")
        break
else:
    print(num,"is prime")    