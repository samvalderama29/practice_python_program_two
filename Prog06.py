# Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

first_num = int(input("Enter number 1: "))

all_minusnum = first_num

for i in range(2,11):
    num = int(input(f"Enter number {i}: "))
    all_minusnum -= num

print(f"Result: {all_minusnum}")