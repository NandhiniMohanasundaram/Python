number=int(input("Enter a num:"))
sum=0
if number<0:
    print("Enter a postive number")
elif number==0:
    print("The sum of digit is",0)
else:
    while number>0:
        rem=number%10
        sum+=rem    
        number=number//10
    print(sum)
