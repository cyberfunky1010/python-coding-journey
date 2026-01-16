# program to reverse a 3-digit number.

num = int(input("enter 3 digit number: "))

if 100 <= num <= 999:
  num1 = num%10  # 6
  rev = num//10 # 25

  num2 = rev % 10  # 5
  num3 = rev //10 # 2

  reverse = num1 * 100 + num2* 10 + num3
  print(reverse)
else:
  print("please enter a 3-digit number !")  