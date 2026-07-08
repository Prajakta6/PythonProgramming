# Design a Python application that creates two threads named EvenFactor and OddFactor.
# • Both threads should accept one integer number as a parameter.
# The EvenFactor thread should:
# • Identify all even factors of the given number.
# • Calculate and display the sum of even factors.
# The OddFactor thread should:
# • Identify all odd factors of the given number.
# • Calculate and display the sum of odd factors.
# After both threads complete execution, the main thread should display the message:
# "Exit from main"

import threading

def EvenFactor(no):
    sum = 0
    print("Even factors are:")
    for i in range(1, no + 1):
        if no % i == 0 and i % 2 == 0:
            print(i)
            sum += i
    print("Sum of even factors =", sum)

def OddFactor(no):
    sum = 0
    print("Odd factors are:")
    for i in range(1, no + 1):
        if no % i == 0 and i % 2 != 0:
            print(i)
            sum += i
    print("Sum of odd factors =", sum)

def main():
    number = int(input("Enter a number: "))

    even_thread = threading.Thread(target=EvenFactor, args=(number,))
    odd_thread = threading.Thread(target=OddFactor, args=(number,))

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

    print("Exit from main")

if __name__ == "__main__":
    main()

#OUTPUT
# Enter a number: 24
# Even factors are:
# Odd factors are:
# 1
# 3
# 2
# 4
# 6
# 8
# 12
# 24
# Sum of even factors = 56
# Sum of odd factors = 4
# Exit from main