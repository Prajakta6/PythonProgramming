# Q2) Count Words in a File
# Problem Statement:
# Write a program which accepts a file name from the user and counts the total number of words in that file.
# Input:
# Demo.txt
# Expected Output:
# Total number of words in Demo.txt

def Count_File_Words(filename):
    fObj = open(filename,"r")
    Data = fObj.read()
    count_words = 0
    for words in Data:
        words = words.split()
        count_words += len(words)
    return count_words

def main():
    filename = input("Enter file name : ")
    words_count = Count_File_Words(filename)
    print(f"Total number of words in {filename} is : {words_count}")

if __name__ == "__main__":
    main()

#OUTPUT
# Enter file name : Demo.txt
# Total number of words in Demo.txt is : 44