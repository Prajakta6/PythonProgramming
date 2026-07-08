import threading #module name

def Display(No1, No2, No3):
    print(f"Inside Display {No1}, {No2}, {No3} : ", threading.get_ident()) # threading.get_ident() -> current thread identification number

def main():
    print("Inside main : ", threading.get_ident()) 

    tobj = threading.Thread(target=Display, args = (11,21,31,)) #new object creation of the class Thread()
    #target=Display => Here target is parameter, Display is function call 
    # (11,21,31,) is a <class 'tuple'>

    tobj.start()

if __name__ == "__main__":
    main()

# OUTPUT
# Inside main :  8263409280
# Inside Display 11, 21, 31 :  6179893248