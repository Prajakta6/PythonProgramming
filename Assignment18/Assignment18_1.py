# Write a program which accept N numbers from user and store it into List. 
# Return addition of all elements from that List.
# Input : Number of elements : 6
# Input Elements: 13 5 45 7 4 56
# Output : 130

def addition_of_elements(data):
    print("Input Elements: ",data)
    sum = 0
    for i in range(0,len(data)):
        sum = sum + data[i]
    return sum

def main():
    number = int(input("Number of elements :"))
    data = []
    for i in range(number):
        user_entered_no = int(input("Enter a number : "))
        data.append(user_entered_no)

    ret = addition_of_elements(data)
    print("Output ",ret)

if __name__ == "__main__":
    main()

#OUTPUT
# Number of elements :6
# Enter a number : 13
# Enter a number : 5
# Enter a number : 45
# Enter a number : 7
# Enter a number : 4
# Enter a number : 56
# Input Elements:  [13, 5, 45, 7, 4, 56]
# Output  130