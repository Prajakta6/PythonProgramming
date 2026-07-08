import sys

if(len(sys.argv) == 3):

    No1 = int(sys.argv[1])
    No2 = int(sys.argv[2])

    Ans = No1 + No2

    print("Addition is : ",Ans)
else:
    print("Invalid number of arguments!")

#OUTPUT

#On Terminal
# (base) prajaktashinde@Prajaktas-MacBook-Pro 5th July 2026 % python CommandLine4.py 10 11      
# Addition is :  21

#OR 

# (base) prajaktashinde@Prajaktas-MacBook-Pro 5th July 2026 % python CommandLine5.py 10
# Invalid number of arguments!