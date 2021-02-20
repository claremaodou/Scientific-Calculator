print('Welcome to the TI 150')
import math # Imports a math function to be able to divide
while True: # Creates a loop
   def add(x, y):  # This function adds two numbers
      return x + y

   def subtract(x, y):  # This function subtracts two numbers
      return x - y

   def multiply(x, y):  # This function multiplies two numbers
      return x * y

   def divide(x, y):  # This function divides two numbers
      return x / y

   def reciprocal(x):  # This function divides 1/x
      return 1 / x


   def square(x):  # This function squares x
      return x ** 2

   def square_root(x):  # This function finds the square root of x
      return math.sqrt(x)

   def scientific_notation(x, y):  # This function calculates scientific notation
      return x * (10 ** y)

   def percent(x):  # This function converts percent into decimal format
      return x / 100

   # Take input from the user
   choice = input("Please enter operator: +, -, *, /, 1/x, x^2, square root, EE (scientific notation), %, exit ")
   while choice not in ['+', '-', '*', '/', '1/x', 'x^2', 'square root', 'EE', '%',
                        'exit']:  # If user input is incorrect then make then choose again
      print ('Invalid Operator, Please Try Again.')
      choice = input("Please enter operator: +, -, *, /, 1/x, x^2, square root, EE (scientific notation), %, exit ")

   if choice == 'exit':  # If user inputs exit then it will stop the code
      print ('BYE!')
      break
   elif choice == '1/x':  # If user inputs 1/x then it allows user to input a x value
      while True:  # creates a loop
         try:
               num3 = int(input('Enter x value: '))  # User inputs x value
         except ValueError:  # If there is a value error (not an integer) then exit function and try again
               print('ERROR. Please Enter a Valid Integer')
               continue
         else:
               break
   elif choice == 'x^2':  # If user inputs x^2 then it allows user to input a x value
      while True:  # creates a loop
         try:
            num3 = int(input('Enter x value: '))  # User inputs value
         except ValueError:  # If there is a value error (not an integer) then exit function and try again
            print('ERROR. Please Enter a Valid Integer')
            continue
         else:
            break
   elif choice == 'square root':  # If user inputs square root then it allows user to input a x value
      while True:  # creates a loop
         try:
            num3 = int(input('Enter x value: '))  # User inputs value
         except ValueError:  # If there is a value error (not an integer) then exit function and try again
            print('ERROR. Please Enter a Valid Integer')
            continue
         else:
            break
   elif choice == 'EE':  # If user inputs EE then it allows user to input x and y value
      while True:  # creates a loop
         try:
            num4 = float(input('Enter x value (can include decimals): '))  # User inputs x value
         except ValueError:  # If there is a value error then exit function and try again
            print('ERROR. Please Enter a Valid Number')
            continue
         else:
            break
      while True:  # creates a loop
         try:
            num5 = int(input('Enter power integer: '))  # User inputs y value
         except ValueError:  # If there is a value error (not an integer) then exit function and try again
            print('ERROR. Please Enter a Valid Integer')
            continue
         else:
            break
   elif choice == '%':  # If user inputs % then it allows user to input a x value
      while True:  # creates a loop
         try:
            num3 = int(input('Enter x value: '))  # User inputs value
         except ValueError:  # If there is a value error (not an integer) then exit function and try again
            print('ERROR. Please Enter a Valid Integer')
            continue
         else:
            break
   elif choice == '+' or '-' or '*' or '/':  # If user inputs + or - or * or / then it allows user to input x and y value
      while True:  # Creates loop
         try:
            num1 = int(input("Enter first number: "))  # User inputs x value
         except ValueError:  # If user input is not an integer
            print('ERROR. Please Enter a Valid Integer')
            continue  # Continue until user inputs valid integer
         else:
            break  # Stops loop once user inputs valid integer
      while True:  # Creates loop
         try:
            num2 = int(input("Enter second number: "))  # User inputs y value
         except ValueError:  # If user input is not an integer
            print('ERROR. Please Enter a Valid Integer')
            continue  # Continue until user inputs valid integer
         else:
            break  # Stops loop once user inputs valid integer

   if choice == '+':  # if user adds
      print('Thank You.', num1, "+", num2, "=", add(num1, num2))  # then print out equation and answer
   elif choice == '-':  # if user subtracts
      print('Thank You.', num1, "-", num2, "=", subtract(num1, num2))  # then print out equation and answer
   elif choice == '*':  # if user multiples
      print('Thank You.', num1, "*", num2, "=", multiply(num1, num2))  # then print out equation and answer
   elif choice == '/':  # if user divides
      try:
         z = num1 / num2
         print('Thank You.', num1, "/", num2, "=", z)  # print out equation and answer
      except ZeroDivisionError:  # if the user tries to divide by 0
         z = 0
         print('Does Not Exist (DNE) -- Can not divide by 0, Please try again')  # print do not exist
   elif choice == '1/x':  # if user uses 1/x
      try:
         print('Thank You.', '1 /', num3, '=', reciprocal(num3))  # print out equation and answer
      except ZeroDivisionError:  # if the user tries to divide by 0
         k = 0
         print('Does Not Exist (DNE) -- Can not divide by 0, Please try again')  # print do not exist
       # user input numbers
   elif choice == 'x^2':
      print('Thank You.', num3, '^2 =', square(num3))  # print out equation and answer
   elif choice == 'square root':
      try:
         print('Thank You.', '√', num3, '=', square_root(num3))  # print out equation and answer
      except ValueError:
         k = 0
         print ('Can not square root a negative number. Please Try Again')
   elif choice == 'EE':
      print('Thank You.', num4, 'x 10^', num5, '=', scientific_notation(num4, num5))
   elif choice == '%':
      print('Thank You.', num3, '% = ', percent(num3))
