
# factorial without function
number=int(input("Enter a num:"))
fact=1
if number < 0:
    print("Enter a positive number")
elif number == 0:
    print("1")
else:
    for i in range(1,number+1):
        fact *=i
    print(fact)


# factorial with function              
def fact(number):
    fact=1
    if number < 0:
        return "Enter a positive number"
    elif number == 0:
        return "1"
    else:
        for i in range(1,number+1):
            fact *=i
        return fact

print(fact(3))
