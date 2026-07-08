# Write a program which accept N numbers from user and store it into List. 
# Accept one another number from user and return frequency of that number from List.
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 5 34 2 5 65
# Element to search : 5
# Output : 3

def search_number(data, search_no):
    print("Input Elements: ",data)
    searched_no_data = []
    for i in data:
        if i == search_no:
            searched_no_data.append(i)
    
    print("Common Elements: ",searched_no_data)
    return len(searched_no_data)

def main():
    number = int(input("Number of elements : "))
    data = []
    for i in range(number):
        user_entered_no = int(input("Input Elements: "))
        data.append(user_entered_no)

    element_to_search = int(input("Element to search : "))
    ret = search_number(data, element_to_search)
    print("Output : ",ret)

if __name__ == "__main__":
    main()

#OUTPUT
# Number of elements : 11
# Input Elements: 13  
# Input Elements: 5
# Input Elements: 45
# Input Elements: 7
# Input Elements: 4
# Input Elements: 56
# Input Elements: 5
# Input Elements: 34
# Input Elements: 2
# Input Elements: 5
# Input Elements: 65
# Element to search : 5
# Input Elements:  [13, 5, 45, 7, 4, 56, 5, 34, 2, 5, 65]
# Common Elements:  [5, 5, 5]
# Output :  3