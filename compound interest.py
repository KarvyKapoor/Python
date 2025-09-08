# Compound Interest
# Taking inputs
P = float(input("Enter the principal amount: "))
R = float(input("Enter the annual interest rate (in %): "))
T = float(input("Enter the time in years: "))
N = int(input("Enter the number of times interest is compounded per year: "))

# Convert rate to decimal
R = R / 100

# Formula
A = P * (1 + R / N) ** (N * T)
CI = A - P

# Output
print("Compound Interest =", round(CI, 2))
print("Total Amount =", round(A, 2))