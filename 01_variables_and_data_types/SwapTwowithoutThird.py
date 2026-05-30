# Swap Two Variables Without a Third
# Given two variables, a and b, swap their values without using a third variable.(tuple unpacking)
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
a, b = b, a #this is called tuple unpacking, it allows us to swap the values of a and b without using a temporary variable.
print(f"The value of a after swapping: {a}")
print(f"The value of b after swapping: {b}")
