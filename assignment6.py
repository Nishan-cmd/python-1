#exercise:6.1
import random
def dice_roller():
    return random.randint(1,6)
def main():
    while True:
        dice = dice_roller()
        print(dice)
        if(dice == 6):
            break

main()


#exercise:6.2
import random

def dice_roller(number_of_sides):
    return random.randint(1,number_of_sides)



def main():
    number_of_sides = int(input("Enter the number of sides on dice: "))
    while True:
        rolled_number = dice_roller(number_of_sides)
        print(rolled_number)
        if(rolled_number == number_of_sides):
            break

main()

#exercise:6.3
def gallons_to_liter(gallons):
    return gallons * 3.7854


def main():
    print("NOTE: Use negative input for Exit!")
    while True:
        gallons = float(input("Enter the volume in gallons: "))
        if (gallons < 0):
            break

        liter = gallons_to_liter(gallons)
        print(f"{gallons} gallons is equal to {round(liter, 2)} Liter.")


main()

#exercise:6.4
def sum_list(int_list):
    return sum(int_list)




def main():
    int_list = [1,2,3,4,5,6,7,8,9,10]
    total = sum_list(int_list)

    print("The sum is "+str(total))

main()


#exercise:6.5
def sum_list(int_list):
    return sum(int_list)




def main():
    int_list = [1,2,3,4,5,6,7,8,9,10]
    total = sum_list(int_list)

    print("The sum is "+str(total))

main()


