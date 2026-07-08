# Design a Python application that creates two threads.
# Thread 1 should compute the sum of elements from a list.
# Thread 2 should compute the product of elements from the same list.
# Return the results to the main thread and display them.

import threading

sum_result = 0
product_result = 1

def Sum(data):
    global sum_result
    for i in data:
        sum_result = sum_result + i

def Product(data):
    global product_result
    for i in data:
        product_result = product_result * i

def main():
    data = []
    size = int(input("Enter number of elements: "))

    for i in range(size):
        no = int(input("Enter number: "))
        data.append(no)

    t1 = threading.Thread(target=Sum, args=(data,))
    t2 = threading.Thread(target=Product, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum =", sum_result)
    print("Product =", product_result)

if __name__ == "__main__":
    main()

#OUTPUT
# Enter number of elements: 5
# Enter number: 2
# Enter number: 3
# Enter number: 4
# Enter number: 5
# Enter number: 6
# Sum = 20
# Product = 720