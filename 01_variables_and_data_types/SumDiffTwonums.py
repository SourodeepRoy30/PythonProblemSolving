# Sum and Difference of Two Numbers
# You are given two integers as input. 
# Your task is to print four results — their sum, their difference, their product, and their quotient.

try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    total      = a + b
    difference = a - b
    product    = a * b

    print(f"Sum:              {total}")
    print(f"Difference:       {difference}")
    print(f"Product:          {product}")

    if b == 0:
        print("Division:         undefined (cannot divide by zero)")
    else:
        print(f"True division:    {a / b}")
        print(f"Floor division:   {a // b}")

except ValueError:
    print("Invalid input. Please enter whole numbers only.")