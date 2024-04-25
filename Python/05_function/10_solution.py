number = int(input("Enter a number to find the factorial: "))
factorial = 1
def fact(number):
    if number == 0:
        return 1
    else:
        factorial = number * fact(number - 1)
        return factorial
fact_of_num = fact(number)
print("Factorial of", number, "is", fact_of_num)