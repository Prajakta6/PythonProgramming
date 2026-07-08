import threading #module name

def Display():
    print("Inside Display : ", threading.get_ident()) # threading.get_ident() -> current thread identification number

def main():
    print("Inside main : ", threading.get_ident()) 

    tobj = threading.Thread(target=Display) #new object creation of the class Thread()
    #target=Display => Here target is parameter, Display is function call

    tobj.start()

if __name__ == "__main__":
    main()

# OUTPUT
# Inside main :  8263409280 #This is parent thread
# Inside Display :  6110441472 #This is child904456777 thread