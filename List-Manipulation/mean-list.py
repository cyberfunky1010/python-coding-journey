# program to calculate mean of a given list of numbers.
# example : [1,2,3,4,5] = 15/5 => mean = 3

lst = eval(input("enter: "))

length = len(lst)

sum = mean = 0

for i in range(length):
    sum += lst[i]
mean = sum / length

print('given list is', lst)
print('*******************')
print('mean of the list is',mean)    