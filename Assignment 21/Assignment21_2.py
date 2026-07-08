# Design a Python application that creates two threads.
# Thread 1 should calculate and display the maximum element from an list.
# Thread 2 should calculate and display the minimum element from the same list.
# The list should be accepted from the user.

import threading

def Maximum(data):
    max_no = data[0]
    for i in data:
        if i > max_no:
            max_no = i
    print("Maximum element =", max_no)

def Minimum(data):
    min_no = data[0]
    for i in data:
        if i < min_no:
            min_no = i
    print("Minimum element =", min_no)

def main():
    data = []
    size = int(input("Enter number of elements: "))

    for i in range(size):
        no = int(input("Enter number: "))
        data.append(no)

    max_thread = threading.Thread(target=Maximum, args=(data,))
    min_thread = threading.Thread(target=Minimum, args=(data,))

    max_thread.start()
    min_thread.start()

    max_thread.join()
    min_thread.join()

    print("Exit from main")

if __name__ == "__main__":
    main()

#OUTPUT
# Enter number of elements: 6
# Enter number: 23
# Enter number: 56
# Enter number: 12
# Enter number: 89
# Enter number: 45
# Enter number: 10
# Maximum element = 89
# Minimum element = 10
# Exit from main