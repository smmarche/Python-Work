# The application displays rates of membership for a library card.
import math
print("Welcome to the Library Management App.")
print("Membership rates")
print("")

days = int(input("Enter the membership number of days: "))
weekly = math.ceil(days / 7)
monthly = math.ceil(days / 30)
quarterly = math.ceil(days / 90)
weekly_rate = (weekly * 10) * 1.0825
monthly_rate = (monthly * 30) * 1.0825
quarterly_rate = (quarterly * 80) * 1.0825

print(f"Weekly membership: {weekly} weeks at ${weekly_rate}")
print(f"Monthly membership: {monthly} months at ${monthly_rate}")
print(f"Quarterly membership: {quarterly} quarters at ${quarterly_rate}")
