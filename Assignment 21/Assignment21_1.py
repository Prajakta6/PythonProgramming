# Design a Python application that creates two threads named Prime and NonPrime.
# Both threads should accept a list of integers.
# The Prime thread should display all prime numbers from the list.
# The NonPrime thread should display all non-prime numbers from the list.

import threading

def ChkPrime(no):
    if no <= 1:
        return False

    for i in range(2, no):
        if no % i == 0:
            return False

    return True

def Prime(data):
    print("Prime numbers are:")
    for i in data:
        if ChkPrime(i):
            print(i)

def NonPrime(data):
    print("Non-prime numbers are:")
    for i in data:
        if not ChkPrime(i):
            print(i)

def main():
    data = []

    size = int(input("Enter number of elements: "))

    for i in range(size):
        no = int(input("Enter number: "))
        data.append(no)

    prime_thread = threading.Thread(target=Prime, args=(data,))
    nonprime_thread = threading.Thread(target=NonPrime, args=(data,))

    prime_thread.start()
    nonprime_thread.start()

    prime_thread.join()
    nonprime_thread.join()

    print("Exit from main")

if __name__ == "__main__":
    main()

#OUTPUT
# Enter number of elements: 8
# Enter number: 11
# Enter number: 12
# Enter number: 13
# Enter number: 15
# Enter number: 17
# Enter number: 18
# Enter number: 19
# Enter number: 20
# Prime numbers are:
# 11
# 13
# 17
# 19
# Non-prime numbers are:
# 12
# 15
# 18
# 20
# Exit from main
