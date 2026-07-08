# Design a Python application that creates two threads named EvenList and OddList.
# Both threads should accept a list of integers as input.
# The EvenList thread should:
# Extract all even elements from the list.
# Calculate and display their sum.
# The OddList thread should:
# Extract all odd elements from the list.
# Calculate and display their sum.
# Threads should run concurrently.

import threading

def EvenList(data):
    sum = 0
    print("Even elements are:")
    for i in data:
        if i % 2 == 0:
            print(i)
            sum += i
    print("Sum of even elements =", sum)

def OddList(data):
    sum = 0
    print("Odd elements are:")
    for i in data:
        if i % 2 != 0:
            print(i)
            sum += i
    print("Sum of odd elements =", sum)

def main():
    data = []

    size = int(input("Enter number of elements: "))

    for i in range(size):
        no = int(input("Enter number: "))
        data.append(no)

    even_thread = threading.Thread(target=EvenList, args=(data,))
    odd_thread = threading.Thread(target=OddList, args=(data,))

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

    print("Exit from main")

if __name__ == "__main__":
    main()

#OUTPUT
# Enter number of elements: 6
# Enter number: 10
# Enter number: 15
# Enter number: 20
# Enter number: 25
# Enter number: 30
# Enter number: 35
# Even elements are:
# 10
# 20
# 30
# Sum of even elements = 60
# Odd elements are:
# 15
# 25
# 35
# Sum of odd elements = 75
# Exit from main