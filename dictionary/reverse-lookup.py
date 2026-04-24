dictionary = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 'random' : 'zero'}

ans = 'y'

while ans == 'y' or ans == 'Y':
    val = input("enter value: ")

    found = False
    for k in dictionary:
        if dictionary[k] == val:
            print("exists at key", k)
            found = True

    if not found:
        print("value does not exist !")

    ans = input("want to enter more (y/n): ")