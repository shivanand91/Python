number = int(input("Enter a number to find factorial: "))
factorial = 1
if number == 0:
    factorial

while number > 0:
    factorial = factorial * number
    number -= 1

print("Factorial: ", factorial)   
#print("factorial of", number, "is", factorial)