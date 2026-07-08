import os #operating system module

def main():
    print("Number of cores are : ", os.cpu_count()) 
    #To Check how many cores are there in your laptop.

if __name__ == "__main__":
    main()

#OUTPUT
# Number of cores are :  8