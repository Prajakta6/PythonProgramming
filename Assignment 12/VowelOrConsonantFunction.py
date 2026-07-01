# Write a program which accepts one character and checks whether it is vowel or consonant.
# Input: a
# Output: Vowel

def check_vowel_or_consonant(character):
    voewels_list = ["a","e","i","o","u"]
    for c in range(0,len(voewels_list)):
        if voewels_list[c] == character:
            return True
       
    return False

def main():
    char = input("Enter a character : ")

    characters = check_vowel_or_consonant(char)

    if(characters == True):
        print("Character '",char, "' is Vowel")
    else:
         print("Character '",char, "' is Consonant")

if __name__ == "__main__":
    main()
