'''
***PART 2***

Write a program that prompts the user to enter a number. The program then prints "Hunter" the number of times the user entered. Use a while loop.

Example of what should appear when the program runs:

Times to print: 3
Hunter
Hunter
Hunter

'''
num = int(input("Enter a number:"))
timestoprint = 0

while timestoprint < num:
  timestoprint += 1
  print("Hunter")
  

