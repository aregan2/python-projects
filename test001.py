import sys
import math

print("This program works with string and numbers")

def reverseString(myString):
    print("\nyou entered a function!\n")
    return myString[::-1]

x = "hel"
y = "lo"
name = input("Enter your name: ")
z = 6
x += y

if(len(name) > 0):
    print(x + " " + name)
    print("here is your name backwards: " + reverseString(name))
    print("your name is " + str(len(name)) + " characters long\n")
else:
    print("the name you entered is not long enough")  
    sys.exit(0)
    
myNum1 = input("Enter a number: ")

if(min(int(myNum1), len(name)) == len(name)):
    print(f"{name} your name is shorter than {myNum1} characters")
else:
    print(f"{name} your name is longer than {myNum1} characters")
    
print("\nAlso the number you entered is equal to " + chr(int(myNum1)) + " in unicode")
print("The square root of " + myNum1 + " is " + str(math.sqrt(int(myNum1))))
print("And " + myNum1 + " squared is " + str(int(myNum1) ** 2))