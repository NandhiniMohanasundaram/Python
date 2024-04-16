number1=int(input("Enter a number :"))
number2=int(input("Enter a number :"))
number3=int(input("Enter a number :"))
if(number1>(number2 and number3)):
    print('The',number1, "is greater among given three numbers")
    exit()
elif(number2>(number3 and number1)):
    print('The',number2, "is greater among given three numbers")
    exit()
elif(number3>(number1 and number2)):
    print('The',number3, "is greater among given three numbers")
    exit()
else:
    print("Enter positive number")
    exit()