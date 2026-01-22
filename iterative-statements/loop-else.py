#program to input some numbers repeatedly and print their sum. the program ends when the user say no more to enter(normal termination)
#or program aborts when the number entered is less than zero.
#loop-else program illustration

count = _sum = 0
ans = 'y'
while ans == 'y':
    num = int(input("enter a number: "))
    if num < 0:
        print("you entered number below zero. aborting !!!")
        break
    _sum = _sum + num
    count = count + 1
    ans = input("want to enter more (y/n): ")

else:
    print("you entered",count,"numbers so far")
print("**************************")
print("sum of the numbers entered is", _sum)

# previous program that show difference between loop-else statement and without one.
# difference is the last statement will run whether the break statemnet runs or not but not incase of loop-else cuz in else part of loop-else if break occurs
# else part will not run  

x = y = z = 0

for a in range(1,6):

    x = int(input("enter x: "))
    y = int(input("enter y: "))
    if y == 0:
        print("zero by division error !!")
        break
    else:
        z = x/y
        print("quotient: ",z)
print("program over !!")    