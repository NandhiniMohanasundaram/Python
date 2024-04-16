import math
print("Select one of the given option")
operator=input("Add\nSub\nMul\nDiv_rem\nDiv_quo\nSquare\nCube\nSqrt: ")
if operator in('Add','Sub','Mul','Div_rem','Div_quo'):
    number1=int(input("Enter a number :"))
    number2=int(input("Enter a number :"))
    if(operator=='Add'):
        Result=number1+number2
        print(Result)
    elif(operator=='Sub'):
        Result=number1-number2
        print(Result)
    elif(operator=='Mul'):
        Result=number1*number2
        print(Result)
    elif(operator=='Div_rem'):
        if(number2!=0):
            Result=number1%number2
            print(Result)
        else:
            print("Error:Division by zero")
            exit()
    elif(operator=='Div_quo'):
        if(number2!=0):
            Result=number1//number2
            print(Result)
        else:
            print("Error:Division by zero")
            exit()
elif(operator=='Square'):
        num=int(input("Enter a number: "))
        Result=num**2
        print(Result)
elif(operator=='Cube'):
        num=int(input("Enter a number: "))
        Result=num**3
        print(Result)
elif(operator=='Sqrt'):
        num=float(input("Enter a number: "))
        Result=math.sqrt(num)
        print(Result)
else:
     print("Enter a valid operation")
     exit()

