P = float(input("Enter principal amount: "))
annual_rate = float(input("Enter annual interest rate (%): "))
N = int(input("Enter loan tenure in months: "))

R = annual_rate / (12 * 100)

power = 1
for i in range(N):
    power = power * (1 + R)

EMI = (P * R * power) / (power - 1)

print("Monthly EMI is:", round(EMI, 2))
