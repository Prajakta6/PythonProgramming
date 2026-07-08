

def Display(*Data):
    print(Data)
    print(type(Data))

def main():
    Display(10,20,30,40,60,False,"Python", 3.14) #We can give any number of arguments here

if __name__ == "__main__":
    main()