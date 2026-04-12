# program to find frequency of all elements. also count duplicates and unique elements in the list.

lst = eval(input("enter list: "))
length = len(lst)

uniq = []
dupl = []

count = i = 0

while i < length:
    element = lst[i]
    count = 1

    if element not in uniq and element not in dupl:
         i+=1
         for j in range(i, length):
             if element == lst[j]:
                count += 1
         else:
             print("element: ", element, "frequency: ", count)
             if count == 1:
                 uniq.append(element)  
             else:
                 dupl.append(element)            
    else:
        i += 1
print("original list: ",lst)        
print("unique list: ",uniq)        
print("duplicate list: ",dupl)        
