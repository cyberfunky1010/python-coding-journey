sum = 0
upper_limit = int(input("enter sum upper limit: "))
for a in range(1,upper_limit+1):
    sum+=a
    print("sum of natural number <=",a,"is",sum)
print("final sum is",sum)    