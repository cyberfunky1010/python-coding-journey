# program that takes 2 inputs and calculate the result based on the operator user chooses.

op = input("enter operator (+ - * / %)")
num1 = float(input("enter num 1: "))
num2 = float(input("enter num 2: "))
result = None

if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    result = num1 / num2
elif op == '%':
    result = num1 % num2
else:
    print("you entered invalid operator")

print(num1,op,num2," = ", result)                    