# String Repetition and Concatenation
# Read a string and a number n from input.
# Print the string repeated n times, and also print it concatenated with itself once.

string = input("Enter a string: ")
n = int(input("Enter a number: "))
# Print the string repeated n times
repeated_string = string * n
print(f"The string repeated {n} times is: {repeated_string}")
# Print the string concatenated with itself once
concatenated_string = string + string
print(f"The string concatenated with itself is: {concatenated_string}")
