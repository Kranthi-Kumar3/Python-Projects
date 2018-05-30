def add(a,b) :
        print(f"\nAddition of {a} and {b} is {a+b}")
    
def sub(a,b) :
    print(f"\nSubtraction of {a} and {b} is {a-b}")
    
def mul(a,b) :
    print(f"\nMultiplication of {a} and {b} is {a*b}")
    
def div(a,b) :
    try :
        print(f"\nDivision of {a} and {b} is {a/b}")
    except ZeroDivisionError :
        print("\nDivide by Zero Error")

#function to select operation    
def operation(choice) :
    a = float(input("Enter Number 1 : "))
    b = float(input("Enter Number 2 : "))
    
    if choice == 1 :
        add(a,b)
    elif choice == 2:
        sub(a,b)
    elif choice == 3:
        mul(a,b)
    elif choice == 4:
        div(a,b)
    else :
        print("\nINVALID CHOICE FOR OPERATION")
    
#main program    
loop = 1 
while loop == 1 :
    print("\n\n\t\tBASIC CALCULATOR")
    print("\t\t----------------\n")
    print("\n\t1.ADDITION\n\t2.SUBTRACTION \n\t3.MULTIPLICATION \n\t4.DIVISION\n")
    operation(int(input("Choose Operation : ")))
    temp = input("Do You Want To Use Calculator Again(1(Yes)/0(No)) : ")
    if temp == '0' :
        loop = 0
    elif temp != '1' :
        print("\nINVALID CHOICE")

print("\n\t\tTHANK YOU _/\_")
    