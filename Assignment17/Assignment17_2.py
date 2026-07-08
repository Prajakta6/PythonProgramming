# Write a program which accept one number and display below pattern.
# Input : 5
# Output :
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

def display_pattern(No):
    for i in range(No):
        for j in range(No):
            print('*', end=" ")
        print("\n")

def main():
    number = int(input("Enter a number : "))
    display_pattern(number)

if __name__ == "__main__":
    main()
