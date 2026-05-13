def calx(x,y):
    return x+y, x-y, x*y, x/y, x%y

num1 = int(input("enter num1 : "))
num2 = int(input("enter num2 : "))

sum, sub, mul, div, mod = calx(x,y)

print(f"sum of {num1} and {num2} is {sum}")
print(f"sub of {num1} and {num2} is {sub}")
print(f"mul of {num1} and {num2} is {mul}")
print(f"div of {num1} and {num2} is {div}")
print(f"mod of {num1} and {num2} is {mod}")