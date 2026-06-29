# Write a program which accepts one number and prints sum of first N natural numbers.
# Input: 5
# Output: 15

def sum_of_natural_nos(no):
    sum = 0
    endNo = no + 1
    for i in range(1,endNo):
        sum = sum + i

    return sum

def main():
    no = int(input("Enter a number : "))
    sum = sum_of_natural_nos(no)
    print(sum)

if __name__ == "__main__":
    main()
