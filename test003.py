import math

print("This program finds the hypotenuse of a right triangle given two side lengths")

def findPythag(a, b):
    a = a ** 2
    b = b ** 2
    return math.sqrt(a + b)
    
def findArea(a, b):
    return str((a * b) / 2)

a = input("Enter a number: ")
b = input("Enter another number: ")
c = findPythag(float(a), float(b))

print("Your triangle has sides of length: " + str(float(a)) + " and " + str(float(b)))
print("And a hypotenuse of length " + str(c))
print("The area of your triangle is " + findArea(int(a), int(b)))