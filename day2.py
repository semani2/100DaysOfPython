# Data Types

# String Integer Float Boolean

# BMI Calculator
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi = float(weight) / (float(height) ** 2)

# print("Your BMI: " + str(round(bmi, 2)))

# F-Strings
print(f"Your BMI: {round(bmi, 2)}")

# Your Life in Weeks

age = input("\nWhat is your current age? ")

remaining_age = 90 - int(age)
print(f"You have {remaining_age * 365} days, {remaining_age * 52} weeks, {remaining_age * 12} months left.")

# Tip Calculator
print("\nWelcome to the Tip Calculator")

bill = float(input("What was the total bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

amount_per_person = (bill/people) * ((tip_percentage/100) + 1.0)

print(f"Each person should pay: ${round(amount_per_person, 2)}")


