# Conditionals

# Even Odd
# print("\nCalculate even or odd")
# num = int(input("Enter a integer"))
#
# if num % 2 == 0:
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")
#
# # BMI 2.0
# print("\n Welcome to BMI 2.0 Calculator")
# height = input("Enter your height in m: ")
# weight = input("Enter your weight in kg: ")
#
# bmi = round(float(weight) / (float(height) ** 2), 2)
#
# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, and you are underweight.")
# elif bmi < 25:
#     print(f"Your BMI is {bmi}, and you have a normal weight.")
# elif bmi < 30:
#     print(f"Your BMI is {bmi}, and you are overweight.")
# elif bmi < 35:
#     print(f"Your BMI is {bmi}, and you are obese.")
# else:
#     print(f"Your BMI is {bmi}, and you are clinically obese.")

# Logical operators
# and or not

print("\n Welcome to the Love Calculator")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

count_t = name1.count("t") + name2.count("t")
count_r = name1.count("r") + name2.count("r")
count_u = name1.count("u") + name2.count("u")
count_e = name1.count("e") + name2.count("e")

count_l = name1.count("l") + name2.count("l")
count_o = name1.count("o") + name2.count("o")
count_v = name1.count("v") + name2.count("v")

percentage_1 = count_t + count_r + count_u + count_e
percentage_2 = count_l + count_o + count_v + count_e

love_score = int(str(percentage_1) + str(percentage_2))

print(f"Your Love Percentage is {percentage_1}{percentage_2}%")


