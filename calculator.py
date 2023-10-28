# python program for simple calculator

# function to add two numbers
def sum(num1, num2):
    return num1 + num2

# function to subract two numbers
def subtract(num1 , num2):
    return num1 - num2

#function to multiply two numbers
def multiply(num1,num2):
    return num1 * num2

# function to divide two numbers
def divide(num1,num2):
    return num1 / num2

print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")

# take the inpu from user
select = int(input("Select the operation from 1,2,3,4 : "))

number_1 = int(input("Enter the 1st number : "))
number_2 = int(input("Enter the 2nd number : "))

if select == 1:
    print(number_1, "+", number_2, "=", sum(number_1, number_2))
    
elif select == 2:
    print(number_1, "-", number_2," = ", subtract(number_1, number_2))
    
elif select == 3 :
    print(number_1 , "*", number_2, " = ",multiply(number_1, number_2))
elif select == 4 :
    print(number_1, "/", number_2, " = ",divide(number_1, number_2))
else:
    print('Invalid input')
    
    
    
    