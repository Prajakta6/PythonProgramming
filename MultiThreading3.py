import threading #module name

def Display(No):
    print(f"Inside Display {No} : ", threading.get_ident()) # threading.get_ident() -> current thread identification number

def main():
    print("Inside main : ", threading.get_ident()) 

    tobj = threading.Thread(target=Display, args = (11,)) #new object creation of the class Thread()
    #target=Display => Here target is parameter, Display is function call

    tobj.start()

if __name__ == "__main__":
    main()

# OUTPUT
# Inside main :  8263409280
# Inside Display : 11  6147616768