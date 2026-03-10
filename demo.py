import math

#HCF
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

num_1 = num1
num_2 = num2

while num2 != 0:
    num1, num2 = num2, num1%num2

HCF = num1

print(f"The HCF of {num_1} and {num_2} is {HCF}")

#LCM
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

LCM = (x*y) // math.gcd(x, y)

print(f"The LCM of {x} and {y} is: {LCM}")

#Palindrome
n = int(input("Enter a random number: "))

original_value = n
reversed_value = 0

while n > 0:
    digit = n%10
    reversed_value = reversed_value*10 + digit
    n //= 10

if original_value == reversed_value:
    print(f"The number {original_value}, is a palindrome")
else:
    print(f"The number {original_value}, is not a palindrome")