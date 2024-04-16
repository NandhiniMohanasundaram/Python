# number=int(input("Enter a number to find its factorial: "))
# fact=1
# for i in range(1,number+1):
#     fact=fact*i
# print("Factorial of " ,number, "is :",fact)

# Recursive Function 

def factorial(number):
    if(number==0 or number==1):
        return 1
    else:
        return number*factorial(number-1)
s=factorial(5)
print(s)
