# Write a program which accepts one number and prints its factors.
# Input: 12
# Output: 1 1 2 3 4 6 12

def find_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def main():
    number = int(input("Enter a number : "))
    Ret = find_factors(number)
    print("Factor of", number , " is : ",Ret)

if __name__ == "__main__":
    main()