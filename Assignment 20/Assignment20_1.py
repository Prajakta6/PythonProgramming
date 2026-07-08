# Design a Python application that creates two separate threads named Even and Odd.
# • The Even thread should display the first 10 even numbers.
# • The Odd thread should display the first 10 odd numbers.
# • Both threads should execute independently using the threading module.
# • Ensure proper thread creation and execution.

import threading

def display_even():
    print("Even numbers:")
    for i in range(2, 21, 2):
        print(i)

def display_odd():
    print("Odd numbers:")
    for i in range(1, 20, 2):
        print(i)

def main():
    even_thread = threading.Thread(target=display_even)
    odd_thread = threading.Thread(target=display_odd)

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

    print("Both threads have finished execution.")

if __name__ == "__main__":
    main()

#OUTPUT
# Even numbers:
# Odd numbers:
# 1
# 3
# 5
# 7
# 2
# 4
# 6
# 9
# 8
# 11
# 10
# 13
# 12
# 15
# 17
# 19
# 14
# 16
# 18
# 20
# Both threads have finished execution.
