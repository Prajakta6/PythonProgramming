# Write a program which accept number from user and print that number 
# of "*" on screen.
#Input 5 Output * * * * *

def display_star(No):
    print("* " * No)

def main():
    number = int(input("Enter a number : "))
    display_star(number)

if __name__ == "__main__":
    main()