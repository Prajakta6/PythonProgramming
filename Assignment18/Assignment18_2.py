# Write a program which accept N numbers from user and store it into List. 
# Return Maximum number from that List.
# Input : Number of elements: 7
# Input Elements: 13 5 45 7 4 56 34
# Output : 56

def check_maximum_number(data):
    print("Input Elements: ",data)
    max_no = data[0]
    for num in data:
        if num > max_no:
            max_no = num
    return max_no

def main():
    number = int(input("Number of elements : "))
    data = []
    for i in range(number):
        user_entered_no = int(input("Input Elements: "))
        data.append(user_entered_no)

    ret = check_maximum_number(data)
    print("Output ",ret)

if __name__ == "__main__":
    main()

#OUTPUT
# Number of elements : 7
# Input Elements: 13
# Input Elements: 5
# Input Elements: 45
# Input Elements: 7
# Input Elements: 4
# Input Elements: 56
# Input Elements: 34
# Input Elements:  [13, 5, 45, 7, 4, 56, 34]
# Output  56