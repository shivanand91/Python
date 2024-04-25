while True:
    number = int(input("Enter number between 1 to 10: "))

    if 1 <= number <= 10:
        print("Valid Number, Thanks!")
        break
    else:
        print("invalid number, try again...")