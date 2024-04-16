# prime without function
number = int(input("Enter num: "))
if number < 0:
    print("Enter a positive number")
elif number == 1:
    print("Neither prime nor composite")
else:
    for i in range(2, number):
        # number%i means if a given number is divisible 
        # by iterable values then it will have more than
        # two factor and thus it is composite
        if number % i == 0:               
            print("Composite")
            break
    else:
        print("Prime")
   


#  prime with function   
def isprime(number):
    if number < 0:
       raise ValueError ("Enter a positive number")
    elif number == 1:
        return "Neither prime nor composite"
    else:
        for i in range(2, number):
            # number%i means if a given number is divisible 
            # by iterable values then it will have more than
            # two factor and thus it is composite
            if number % i == 0:               
                return "Composite"
                
        else:
            return"Prime"


# function call 
n=2
print(isprime(n))

#another way    
print(isprime(4))
