#exercise-4.1
number = 1

while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1

#exercise-4.2
while True:
    inches = float(input("Enter inches (negative number to stop): "))

    if inches < 0:
        print("Program ended.")
        break

    centimeters = inches * 2.54
    print(f"{inches} inches = {centimeters} cm")

#exercise-4.3
smallest = None
largest = None

while True:
    user_input = input("Enter a number (or press Enter to quit): ")

    if user_input == "":
        break  # stop the loop if input is empty

    try:
        number = float(user_input)  # convert input to a number
    except ValueError:
        print("Please enter a valid number.")
        continue  # ask again if input is invalid

    # Set smallest and largest
    if smallest is None or number < smallest:
        smallest = number
    if largest is None or number > largest:
        largest = number

# Print results
if smallest is None:
    print("No numbers were entered.")
else:
    print(f"Smallest number: {smallest}")
    print(f"Largest number: {largest}")

#exercise-4.4
import random
computer_guess = random.randint(1,10)

while True:
    user_guess = int(input("Guess the number from 1 to 10: "))
    if(user_guess<computer_guess):
        print("Too Low!")
    elif(user_guess>computer_guess):
        print("Too High!")
    else:
        print("Correct!")
        break

#exercise-4.5
username = "user"
password = "admin"

count = 1

while True:
    entered_username = input("Enter username: ")
    entered_password = input("Enter password: ")
    if(entered_username == username and entered_password == password):
        print("Welcome!")
        break
    elif(count >= 5):
        print("Access Denied!")
        break
    else:
        print(f"Wrong credentials. Please Enter Again, remaining attempts: ({5-count})")
    count+=1