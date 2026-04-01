# program to find minimum element from a list along with its index.

lst = eval(input("enter a list: "))
length = len(lst)

min_element = lst[0]
min_index = 0

for i in range(1,length):
    if lst[i] < min_element:
        min_element = lst[i]
        min_index = i

print("given list is : ", lst)
print("the minimum element of the given list is : ")
print(min_element, "at index ", min_index)

