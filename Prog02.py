# Prog02: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.

num1 = int(input("First number: "))
num2 = int(input("Second number: "))

notequalnum = "NOT EQUAL" if num1 != num2 else "EQUAL"

print(notequalnum)