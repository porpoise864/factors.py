# Author: Sarah Oertly
# Date: 10/16/2019
# Description: Write a program that asks the user to enter a positive integer, then prints a list of all positive
# integers that divide that number evenly, excluding itself and 1, in ascending order. When you run your program, it
# should match the following format:
number = int(input("Please enter a positive integer: "))
for i in range(1, number + 1):
    if number % i == 0:
        print(i, end=" ")
