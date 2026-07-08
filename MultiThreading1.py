import threading #module name

def Display():
    print("Inside Display : ", threading.get_ident()) # threading.get_ident() - current thread identification number

def main():
    print("Inside main : ", threading.get_ident())
    Display()

if __name__ == "__main__":
    main()

# OUTPUT
# Inside main :  8263409280
# Inside Display :  8263409280