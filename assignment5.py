#exercise-5.1
import random

number_of_dice = int(input("Enter the number of dice to roll: "))
total = 0

for i in range(number_of_dice):
    total += random.randint(1,6)

print(f"The total of {number_of_dice} rolled dice is {total}")

#exercise-5.2
numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    if user_input == "":
        break
    numbers.append(float(user_input))

numbers.sort(reverse=True)
top_five = numbers[:5]

print("The five greatest numbers are:")
for num in top_five:
    print(num)

#exercise-5.3
number= int(input("Enter number to be checked as prime: "))
factors = 0

for i in range(1,number+1):
    if(number%i==0):
        factors += 1

if number <=1:
    print(f"{number} is not a prime number!")

elif factors > 2:
    print(f"{number} is not a prime number!")
else:
    print(f"{number} is a prime number!")

#exercise-5.4
cities = []
for i in range(5):
    city = input(f"Enter city number {i+1}: ")
    cities.append(city)

for city in cities:
    print(city)