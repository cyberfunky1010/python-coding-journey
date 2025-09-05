# program to reverse a 3-digit number.

num = int(input("enter 3 digit number: "))

num1 = num%10  # 6
rev = num//10 # 25

num2 = rev % 10  # 5
num3 = rev //10 # 2
print(num1,num2,num3)