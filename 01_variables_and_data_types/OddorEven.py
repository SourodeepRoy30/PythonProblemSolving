# Check if a Number is Even or Odd
# Given an integer, determine if it is even or odd and print the result.
# Check if a Number is Even or Odd

try:
    number = int(input("Enter an integer: "))
    
    if number == 0:
        print("0 is neither even nor odd.")
    elif number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")

except ValueError:
    print("Invalid input. Please enter a whole number.")