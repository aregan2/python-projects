print("This program works with arrays")

delimChar = "$"
cars = []
name = ""

print("Use '" + delimChar + "' to stop entering brands\n")
while(name != delimChar):
    name = input("Enter a car brand: ")
    if(name == delimChar):
        break
    cars.append(name)
    
print("You entered " + str(len(cars)) + " brands!\n")

print("Here they are: ")
for x in cars:
    print(x)
    
print("")

x = len(cars) - 1
while(cars):
    print(cars[x] + " is removed from the array")
    cars.pop(x)
    x -= 1
    
print("\nThe array is now empty")