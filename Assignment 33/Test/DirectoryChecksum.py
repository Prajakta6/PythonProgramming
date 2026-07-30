import sys
import os
import hashlib

def CalculateChecksum(FileName):
    
    fObj = open(FileName, "rb") #rb is binary I/O
    
    hObj = hashlib.md5() #hashlib is a module and md5 is a algorithm

    Buffer = fObj.read(1024) #Reading 1024 bytes - 1 kb

    while(len(Buffer) > 0):
        hObj.update(Buffer)
        Buffer = fObj.read(1024) #Again reading next 1024 bytes. At the end Buffer will be 0 so loop will end

    fObj.close()

    return hObj.hexdigest() #calculating checksum of whole file data

def FindDuplicate(DirectoryName):

    Ret = False
    Ret = os.path.exists(DirectoryName)
    if Ret == False:
        print("Path is invalid!")
        return

    Ret = os.path.isdir(DirectoryName)

    if Ret == False:
            print("It is not a Directory")
            return
    
    for FolderName, SubFolder, Filename in os.walk(DirectoryName):
        for fName in Filename:
            fName = os.path.join(FolderName,fName)
            Checksum = CalculateChecksum(fName)
            print(f"{fName} : {Checksum}")

def main():
    FindDuplicate("Marvellous")

if __name__ == "__main__":
    main()

#OUTPUT
# Checksum of file is :  1a88f20756104dd343405e22464dac42
# This is 32 character lower case hex string checksum