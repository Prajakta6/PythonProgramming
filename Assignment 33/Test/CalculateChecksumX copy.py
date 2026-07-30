import sys
import os
import hashlib

def CalculateChecksum(FileName):
    
    fObj = open(FileName, "rb") #rb is binary I/O
    
    hObj = hashlib.md5() #hashlib is a module and md5 is a algorithm

    Buffer = fObj.read(1000) #Reading 1000 bytes

    while(len(Buffer) > 0):
        hObj.update(Buffer)
        Buffer = fObj.read(1000) #Again reading next 1000 bytes. At the end Buffer will be 0 so loop will end

    fObj.close()

    return hObj.hexdigest() #calculating checksum of whole file data


def main():
    Ret = CalculateChecksum("DemoX.txt")
    print("Checksum of file is : ",Ret)

if __name__ == "__main__":
    main()

#OUTPUT
# Checksum of file is :  1a88f20756104dd343405e22464dac42 
# This is 32 character lower case hex string checksum