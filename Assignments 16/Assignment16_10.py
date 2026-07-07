# Write a program which accept name from user and display length of its name.
# Input : Marvellous
# Output : 10

def display_even_numbers(name):
    print(len(name))

def main():
    name = input("Enter name : ")
    display_even_numbers(name)

if __name__ == "__main__":
    main()