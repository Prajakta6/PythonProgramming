# Write a program which display first 10 even numbers on screen.
# Output : 2 4 6 8 10 12 14 16 18 20

def display_even_numbers():
    for i in range(2, 21, 2):
        print(i)

def main():
    display_even_numbers()

if __name__ == "__main__":
    main()