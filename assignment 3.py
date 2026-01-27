#exercise 3.1
length = int(input("Enter the length of the zander in centimeters : "))
if length < 42:
    difference = 42 - length
    print("the zander is small, release the fish.")
    print("it is", difference, "cm below the size limit.")

else:
    print("the zander meets the size limit.")

#exercise 3.2
cabin = input("enter your cabin name: ")
if cabin == "lux":
    print("upper-deck cabin with a balcony ")
elif cabin == "a":
    print("above the car deck, equipped with a windows")
elif cabin == "b":
    print("windowless cabin above the car deck ")
elif cabin == "c":
    print("windowless cabin below the car deck ")
else:
    print("invalid cabin class")

#exercise 3.3
gender = input("enter your biological gender (male or female): ")
hemoglobin = int(input("enter your hemoglobin value(g/l): "))
if gender == "male":
    if hemoglobin < 134:
        print("your hemoglobin level is low.")
    elif hemoglobin <= 167:
        print("your hemoglobin level is normal.")
    else:
        print("your hemoglobin level is high.")
        if gender == "female":
            if hemoglobin < 177:
                print("your hemoglobin level is low.")
            elif hemoglobin <= 155:
                print("your hemoglobin level is normal.")
            else:
                print("your hemoglobin level is high.")


#exercise 3.4
year = int(input("enter a year: "))
if year % 4 == 0:
    print("the year is leap year.")
elif year % 100 == 0:
        print("the year is leap year.")
elif year % 400 == 0:
    print("the year is leap year.")
else :
    print("the year is not a leap year.")