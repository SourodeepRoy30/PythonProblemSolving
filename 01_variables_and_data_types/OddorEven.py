# Check if a Number is Even or Odd
# Given an integer, determine if it is even or odd and print the result.

number = int(input("Enter an integer: "))
if number % 2 == 0:
    print(f"{number} is an even number.")
elif number % 2 != 0:
    print(f"{number} is an odd number.")
elif number == 0:
    print("0 is neither even nor odd.")
else:
    print("Invalid input.")