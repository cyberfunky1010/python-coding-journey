#program that store marks details of students and print output as:

# Name
# muhammad
# Subject(keys)         Marks(values)
# 1                      40
# 2                      50              
# 3                      60             

d1 = {1:40, 2:70, 3:70}
d2 = {1:40, 2:50, 3:60}
d3 = {1:70, 2:80, 3:90}
d4 = {'john':d1, 'ibrahim':d2, 'muhammad':d3}

for x in d4:
    print('name')
    print(x)
    print('Subjects(key)', '\t', 'Marks(value)')
    for y in d4[x].keys():
        print(y, '\t\t',d4[x][y])
    print()    