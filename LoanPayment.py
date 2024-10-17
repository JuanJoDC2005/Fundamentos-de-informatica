
P = 250000  # Loan amount in €
annual_rate = 5 / 100  # Annual interest rate
years = 30  # Loan term in years

r = annual_rate / 12  # Monthly interest rate
n = years * 12  # Total number of payments

# Calculate monthly payment using the formula
M = P * (r * (1 + r) ** n) / ((1 + r) ** n - 1)

print(f"The monthly payment (M) is: {M:.2f}€")
