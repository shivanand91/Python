limit = int(input("Enter a limit to find Even Number: "))
def even_gen(limit):
    for i in range(2, limit + 1, 2):
       yield i

for num in even_gen(limit):
    print(num)