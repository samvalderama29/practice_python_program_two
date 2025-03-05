# Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if num1 > num2:
    for between_num in range(num1, num2 - 1, -1):
        print(between_num)
else:
    for between_num in range(num1, num2 + 1):
        print(between_num)