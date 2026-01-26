rows = int(input("enter number of rows: "))

for i in range(1, rows + 1):       #control rows 
    for space in range(rows-i):    #shift spaces- centers the stars 
        print(end="  ")

    for star in range(2*i-1):      #star loop   (2*i-1 prints star in odd number 1,3,5,6...form a triangle)
        print("* ", end="")
    
    print()                        #moves cursor to the next line