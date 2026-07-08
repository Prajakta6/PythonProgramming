# Nested/Inner Function 
# OOP - Abstraction - Hiding something from outside world
# Here Amul function is defined inside BigBazar function

def BigBazar():
    print("Inside BigBazar")
    def Amul():
        print("Inside Amul Ice-Cream Parlour")

    Amul()

def main():
   BigBazar() # Allowed

if __name__ == "__main__":
    main()