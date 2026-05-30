# Simple Interest Calculator
# Given the principal amount, rate of interest, and time period, calculate and print the simple interest 
# using the formula: SI = (P * R * T) / 100.
principal = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest: "))
time_period = float(input("Enter the time period in years: "))
# Calculate simple interest
simple_interest = (principal * rate_of_interest * time_period) / 100
print(f"The simple interest is: {simple_interest:.2f}")
