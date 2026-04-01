# program to slice two different lists from a list and perform sum and average of the sliced lists respectively.

lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

lst1 = lst[5:15:2]
lst2 = lst[::4]

sum = avg = 0

print("slice 1")

for a in lst1:
    sum+=a
print("sum: ", sum)


print()
print("******************")

print("slice 2")
print()

sum = 0
for a in lst2:
    sum+=a
    
print("sum: ",sum)

avg = sum/len(lst2)

print("average: ", avg)


    
