# Design a Python application that creates three threads named 
# Small, Capital, and Digits.
# All threads should accept a string as input.
# The Small thread should count and display the number of lowercase characters.
# The Capital thread should count and display the number of uppercase characters.
# The Digits thread should count and display the number of numeric digits.
# Each thread must also display:
# Thread ID
# Thread Name

import threading

def Small(text):
    count = 0
    for ch in text:
        if ch.islower():
            count += 1

    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Lowercase characters:", count)
    print()

def Capital(text):
    count = 0
    for ch in text:
        if ch.isupper():
            count += 1

    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Uppercase characters:", count)
    print()

def Digits(text):
    count = 0
    for ch in text:
        if ch.isdigit():
            count += 1

    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Digits:", count)
    print()

def main():
    string = input("Enter a string: ")

    small_thread = threading.Thread(target=Small, args=(string,))
    capital_thread = threading.Thread(target=Capital, args=(string,))
    digits_thread = threading.Thread(target=Digits, args=(string,))

    small_thread.start()
    capital_thread.start()
    digits_thread.start()

    small_thread.join()
    capital_thread.join()
    digits_thread.join()

    print("Exit from main")

if __name__ == "__main__":
    main()

#OUTPUT
# Enter a string: Marvellous123Infosystems
# Thread ID: 6140309504
# Thread Name: Thread-1 (Small)
# Lowercase characters: 19

# Thread ID: 6157135872
# Thread ID: 6173962240
# Thread Name: Thread-2 (Capital)
# Thread Name: Thread-3 (Digits)
# Digits: 3

# Uppercase characters: 2

# Exit from main