# count number of pairs if both are even in a nested tuple. 

tup = ( (2,5), (4,2), (9,8), (12,10), (2,10) )

count = 0          

for i in range(len(tup)):
    a, b = tup[i]                      # unpacking the pair
    if a % 2 == 0 and b % 2 == 0:      # checking if both elements are even. 
        count += 1                     # increasing count if even

print("count is", count)