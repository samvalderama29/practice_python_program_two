# Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.

num1 = int(input("First number: "))
num2 = int(input("Second number: "))

smallnum = f"{num1} is Smaller" if num1 < num2 else f"{num2} is Smaller"

print(smallnum)