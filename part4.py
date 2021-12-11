'''
***PART 4***

Write a program that repeatedly prompts the user to enter numbers until the user enters 0. The program calculates the product of all of the entered numbers and prints the product.

Example of what should appear when this part runs:

Enter a number or enter 0 to stop: 2
Enter a number or enter 0 to stop: 3
Enter a number or enter 0 to stop: 10
Enter a number or enter 0 to stop: 0
Product: 60

'''
num1 = int(input("Enter a number or enter 0 to stop:"))
product = 0
num2 = 1

if num1 != 0:
  while num2 != 0 and num1 != 0:
    num2 = int(input("Enter a number or enter 0 to stop:"))
    product = num2 * num1
    if num2 == 0:
      print(product)
      break
    num1 = int(input("Enter a number or enter 0 to stop:"))
    product = num2 * num1
    if num1 == 0:
      print(product)
      break
else:
  print("Product: 0")


#if num2 != 0 and num1 != 0:
      
  #elif num2 == 0 or num1 == 0:
    #print("Product:", product)
