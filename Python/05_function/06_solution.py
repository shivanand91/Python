number_one = int(input("Enter number one: "))
number_two = int(input("Enter number two: "))
num_x = int(input("Enter a number for cube: "))

def add(a, b):
    return a + b

result = add(number_one, number_two)
print("sum of two number is ", result)

cube = lambda x: x ** 3
print("Cube of", num_x, "is", cube(num_x))