 #add numbers
'''
num1 = int(input("Enter the First number for addition :"))
num2 = int(input("Enter the Second Number for addition :"))

sum_result = num1 + num2
print(f"Addition Results of {num1} + {num2} =  {sum_result}")





'''

'''
num1 = int(input("Enter a number:")) 
num12 = int(input("Enter a number: "))

result = num1 ** num12
print(f"Results of {num1} ** {num12} = {result}   ") 


'''
'''
num3 = int(input("Enter the first number for division : "))
num4 = int(input("Enter the second number for division :"))

if num4 == 0:
  print("Error! : Division by zero is not possible")
else:
  result = num3 / num4
  print(f"Division: {num3} / {num4} = {result}")

'''


#area of the triangle
'''
base = int(input("Enter the base of the triangle: "))
height = int(input("Enter the height of the triangle: "))

area = 0.5 * base * height
print(f"The area of the triangle is: {area}")

'''

#swapping 2 variables
'''  
e = input("Enter a value for a :")
k = input("Enter a value for b :")
print(f"Original values: a = {e} b = {k}")

fake = e
e = k
k = fake
print(f"Swapped values: a = {e} b = {k}")

'''

#random numbers
'''
import random
print(f"random no: {random.randint(1,3)}")
'''


#kilometers to miles (1 kilometers = 0.621371 miles)
'''
kilometers = float(input("Enter a distance in Kilometers:"))
conv = 0.621371
miles = kilometers * conv
print(f" {kilometers} Kilometers is = {miles} Miles")
'''
