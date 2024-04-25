table = int(input("Enter number to print table: "))

for i in range(1, 11):
    if i == 5:
        continue
    else:
        final_table = table * i
        print( table, 'X', i, '=', final_table)