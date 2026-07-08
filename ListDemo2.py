def main():
    Data = [10,20,30,40] #Data type = list

    print(type(Data))
    print(len(Data))
    
    print(Data[0])
    print(Data[1])
    print(Data[2])
    print(Data[3])

    Data[1] = 21 #Update the data at position 1
    print(Data[1])

    

if __name__ == "__main__":
    main()