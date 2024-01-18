# Day 2
# January 18, 2024
# Author: Ratn Govindam
# #100DaysofCoding

# Lesson 5 Day 2 - Data Types
two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
sum = 0
for ch in two_digit_number:
  num = int(ch)
  sum += num
print(sum)
# Or another code
first_number = int(two_digit_number[0])
second_number = int(two_digit_number[1])
sum = first_number + second_number
print(sum)

# Lesson 6 Day 2 - BMI Calculator
# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
height_float = float(height)
bmi = int(float(weight) / (height_float*height_float))
print(bmi)

# Lesson 7 Day 2 - LIFE IN WEEKS
age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
exact_age_left = 90 - int(age)
no_of_weeks_in_an_year = 52
total_weeks_left = exact_age_left * no_of_weeks_in_an_year
print(f'You have {total_weeks_left} weeks left.')

# Day 2 Completed!
# Happy Coding🧡🤍💚
