character = input("Enter a character: ")
number = int(input("Enter a number to multiply with character: "))

def char_numtiply(character, number):
    result = character * number
    return result

final_result = char_numtiply(character, number)
print("Multiplication of ", character, "and", number, "is", final_result)