#exercise 2.1
name = input('What is your name? ')
print('Hello, ' + name +"!")

#exercise 2.2
radius = float(input("Enter the radius of circle: "))
area = 3.14159*radius*radius
print("The area of the circle is ", area)

#exercise 2.3
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
perimeter = 2 * (length + width)
area = length * width
print("the perimeter of the circle is: ", perimeter)
print("the area of the circle is: ", area)

#exercise 2.4
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
num_3 = int(input("Enter the third number: "))

sum_nums = num_1 + num_2 + num_3
product = num_1 * num_2 * num_3
average = sum_nums / 3

print("sum: ", sum_nums)
print("product: ", product)
print("average: ", average)

#exercise 2.5
talent = float(input("enter talent: "))
pound = float(input("enter pound: "))
lot = float(input("enter lot: "))
total_lot = talent * 20 * 32 + pound * 32 + lot
total_grams = total_lot * 13.3
kilograms = int(total_grams // 1000)
grams = total_grams % 1000
print("the weight is", kilograms, "kilograms and", grams, "grams." )

#exercise 2.6
import random
code1 = random.randint(0, 9), random.randint(0,9), random.randint(0,9)
code2 = random.randint(1, 6), random.randint(1,6), random.randint(1,6), random.randint(1,6)
print("three-digit lock code", code1)
print("four-digit lock code", code2)