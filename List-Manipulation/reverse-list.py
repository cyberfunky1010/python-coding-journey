# program that reverses an array of integers (in place). in place - no new copy, does not create a new list, instead rearranges the original list making 
# it memory efficienct. 

lst = eval(input("enter a list of intergers: "))

# set two pointers one at start and one at end.
left = 0
right = len(lst) - 1

while left < right:
    
    # swapping the elements.
    lst[left], lst[right] = lst[right], lst[left]
    
    # moving the pointers towards center
    left += 1
    right -= 1

print(lst)    