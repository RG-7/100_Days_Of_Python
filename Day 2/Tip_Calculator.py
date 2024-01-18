# Day 2 ClassWork
# January 18, 2024
# Author: Ratn Govindam

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print('Welcome to the tip Calculator.')
total_bill = float(input('What was the total bill?'))
number_of_person = int(input('How many people to split the bill? '))
tip = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
percent = (tip/100)*total_bill
each_person_should_pay = (total_bill  + percent)/ number_of_person
print(f'{each_person_should_pay:.2f}')
