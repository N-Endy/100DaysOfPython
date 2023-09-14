# Input current age
# Subtract age from 90 years
# Get days, weeeks and months in remainder

age = int(input("What is your current age?: "))
age_left = 90 - age
age_in_days = age_left * 365
age_in_weeks = age_left * 52
agein_months = age_left * 12

print(f"You have {age_in_days} days, {age_in_weeks} weeks, and {agein_months} months left.")