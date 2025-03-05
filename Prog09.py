# Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.

for zerofive_num in range(101):
    if zerofive_num % 10 != 0 and zerofive_num % 10 != 5:
        print(zerofive_num)