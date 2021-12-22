
# -*- coding: utf-8 -*-
"""
Created by Jamal Hosein shah

"""

def add(x, y):
   """This function adds two numbers"""

   return x + y

def subtract(x, y):
   """This function subtracts two numbers"""

   return x - y

def multiply(x, y):
   """This function multiplies two numbers"""

   return x * y

def divide(x, y):
   """This function divides two numbers"""
   
   return x / y
   
def Exponent(x, y):
    """This funciton is exponent two numbers"""
    
    return x ** y

   

# take input from the user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exponent")

choice = input("Enter choice(1/2/3/4/5):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
   
elif choice == '5':
   print(num1,"*",num2,"=", Exponent(num1,num2))
else:
   print("Invalid input")
   
 
 ######################### out put ##################################

###### 1 EXAMPLE (Addition)

Select operation.
1.Add
2.Subtract
3.Multiply
4.Divide
5.Exponent

Enter choice(1/2/3/4/5):1

Enter first number: 23

Enter second number: 34
23 + 34 = 57


###### 2 Example (Multiplication)

Select operation.
1.Add
2.Subtract
3.Multiply
4.Divide
5.Exponent

Enter choice(1/2/3/4/5):3

Enter first number: 34

Enter second number: 23
34 * 23 = 782


###### 3 Example (Division)

Select operation.
1.Add
2.Subtract
3.Multiply
4.Divide
5.Exponent

Enter choice(1/2/3/4/5):4

Enter first number: 4566

Enter second number: 3
4566 / 3 = 1522.0

##### 4 Example (Exponent)

Select operation.
1.Add
2.Subtract
3.Multiply
4.Divide
5.Exponent

Enter choice(1/2/3/4/5):5

Enter first number: 3

Enter second number: 4
3 * 4 = 81


# 5 Example (Subtraction)

Select operation.
1.Add
2.Subtract
3.Multiply
4.Divide
5.Exponent

Enter choice(1/2/3/4/5):2

Enter first number: 4566

Enter second number: 345
4566 - 345 = 4221


