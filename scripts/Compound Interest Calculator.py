
def compound_interest(P, r, n, t):
    return P * (1 + r/n) ** (n * t)

P = float(input("Starting amount: "))
r = float(input("Interest rate (decimal): "))
n = int(input("Compounds per year: "))
t = float(input("Years: "))

final_amount = compound_interest(P, r, n, t)
print("Future value:", round(final_amount, 2))

