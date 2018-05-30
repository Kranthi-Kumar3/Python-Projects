#Function to check whether a number is prime or not
def isPrime(n) :
    for i in range(3,n,2) :
        if n%i == 0 :
            return 0
    return 1    

#main program
n = int(input("Enter Number : "))

if n == 2:
    print(f"{n} is a Prime Number")
elif n%2 != 0 :
    if isPrime(n) :
        print(f"{n} is a Prime Number")
    else :
        print(f"{n} is NOT a Prime Number")
else :
    print(f"{n} is NOT a Prime Number")