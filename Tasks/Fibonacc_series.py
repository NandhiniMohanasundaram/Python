
# FibonacciSeries with function
number=int(input("Enter a range:"))
if (number<1):
    print("Enter positive number")
elif (number==1):
    print(0)
elif (number==2):
    print(0)
    print(1)
else:
    first=0
    second=1
    print(first)
    print(second)
    for i in range(3,number+1):
        third=first+second
        print(third)
        first,second=second,third



# FibonacciSeries with function
def fibonacciSeries(number):
    if (number<1):
       return "Enter positive number"
    elif (number==1):
        return "0"
    elif (number==2):
        return "0/n1"
        
    else:
        first=0
        second=1
        result="0\n1"
        for i in range(3,number+1):
            third=first+second
            result+= f"\n{third}"
            first,second=second,third
        return result

print(fibonacciSeries(3))
            