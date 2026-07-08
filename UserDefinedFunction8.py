#Nested Function

def BigBazar():
    print("Inside BigBazar")
    def Amul():
        print("Inside Amul Ice-Cream Parlour")

def main():
   BigBazar() # Allowed
   Amul() # NameError: name 'Amul' is not defined
   BigBazar.Amul() # AttributeError: 'function' object has no attribute 'Amul'


if __name__ == "__main__":
    main()