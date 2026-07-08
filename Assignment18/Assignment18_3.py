# Write a program which accept N numbers from user and store it into List. 
# Return Minimum number from that List.
# Input : Number of elements : 4
# Input Elements : 13 5 45 7
# Output : 5

def check_minimum_number(data):
    print("Input Elements: ",data)
    min_no = data[0]
    for num in data:
        if num < min_no:
            min_no = num
    return min_no

def main():
    number = int(input("Number of elements : "))
    data = []
    for i in range(number):
        user_entered_no = int(input("Input Elements: "))
        data.append(user_entered_no)

    ret = check_minimum_number(data)
    print("Output ",ret)

if __name__ == "__main__":
    main()

#OUTPUT
# Number of elements : 4
# Input Elements: 13
# Input Elements: 5
# Input Elements: 45
# Input Elements: 7
# Input Elements:  [13, 5, 45, 7]
# Output  5