# Write a program which accepts one number and prints multiplication table 
# of that number.
# Input: 4
# Output:
# 4 8 12 16 20 24 28 32 36 40

def multiplication_table(no):
    multi = 0
    table = []
    for i in range(1,11):
        multi = no * i
        table.append(multi)

    return table

def main():
    table = multiplication_table(4)
    print(table)

if __name__ == "__main__":
    main()