# Design a Python application that creates two threads named Threadl and Thread2.
# Threadl should display numbers from 1 to 50.
# Thread2 should display numbers from 50 to 1 in reverse order.
# Ensure that:
# Thread2 starts execution only after Threadl has completed.
# Use appropriate thread synchronizatio

import threading

def Thread1():
    print("Numbers from 1 to 50:")
    for i in range(1, 51):
        print(i)

def Thread2():
    print("Numbers from 50 to 1:")
    for i in range(50, 0, -1):
        print(i)

def main():
    t1 = threading.Thread(target=Thread1)
    t2 = threading.Thread(target=Thread2)

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()

#OUTPUT
# Numbers from 1 to 50:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
# 21
# 22
# 23
# 24
# 25
# 26
# 27
# 28
# 29
# 30
# 31
# 32
# 33
# 34
# 35
# 36
# 37
# 38
# 39
# 40
# 41
# 42
# 43
# 44
# 45
# 46
# 47
# 48
# 49
# 50
# Numbers from 50 to 1:
# 50
# 49
# 48
# 47
# 46
# 45
# 44
# 43
# 42
# 41
# 40
# 39
# 38
# 37
# 36
# 35
# 34
# 33
# 32
# 31
# 30
# 29
# 28
# 27
# 26
# 25
# 24
# 23
# 22
# 21
# 20
# 19
# 18
# 17
# 16
# 15
# 14
# 13
# 12
# 11
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# Exit from main