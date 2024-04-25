def square_of_number(number):
    result = number ** 2
    return result
num_square = int(input("Enter a number: "))
final_Result = square_of_number(num_square)
print("square of ", num_square, "is", final_Result)
# print("square of ", num_square, "is", square_of_number(num_square))