# using for loop

odd_sum = 0
even_sum = 0

num = int(input("enter a number: "))

for a in range(2,num+1,2):
    even_sum+=a
print("even sum: ",even_sum)    

for a in range(1, num+1,2):
    odd_sum+=a
print("odd sum: ",odd_sum)

print()
print("now using while loop")
print()

# using while loop.

n = int(input("enter a number: "))
ctr = 1

sum_even = sum_odd = 0

while ctr <= n:
    if ctr%2 == 0:
        sum_even+=ctr
    else:
        sum_odd+=ctr
    ctr+=1

print("even sum: ",sum_even)
print("odd sum: ",sum_odd)