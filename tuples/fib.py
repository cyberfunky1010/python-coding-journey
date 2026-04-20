# program to create tuple that stores fibonacci series up 9.

n = 10 # number of terms

fib_list = [0,1]   # since we can't modify a tuple, we're using a list to add elements

for i in range(2,n):
    fib_list.append(fib_list[-1] + fib_list[-2]) # add the sum of last two elements to the list.

fib_tuple = tuple(fib_list)   # convert list to tuple. 

print(fib_tuple)