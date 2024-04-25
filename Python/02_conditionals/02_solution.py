day = input("Enter The Day: ")
age = int(input("Enter your age: "))
# Method 1
price = 12 if age >= 18 else 8

if day == "wednesday":
    price = price - 2
    #price -= 2

print("your movie ticket price is:", price)

# Method 2
# price = 12
# if age <18:
#     print("your movie ticket price is: ", price - 4)
# else:
#     print("your movie ticket price is: ", price)

        
