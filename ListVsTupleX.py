#Explain difference between List and Tuple. (Interview question)

# _________________________________
#             List      Tuple
# _________________________________
# Ordered      Yes      Yes
# Indexed      Yes      Yes
# Mutable      Yes      No
# Hetrogeneous Yes      Yes
# _________________________________


def main():
    Data1 = [10,3.14,True,"Pune"] #List is hetrogeneous. i.e. Different data type 
    Data2 = (10,3.14,True,"Pune") #Tuple is hetrogeneous. i.e. Different data type 

    print(Data1)
    print(Data2)

    print(Data1[0])
    print(Data2[0])

if __name__ == "__main__":
    main()