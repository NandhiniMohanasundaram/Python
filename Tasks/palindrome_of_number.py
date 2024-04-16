number=int(input("Enter a  num:"))
reversed=0
if number<0:
    print("Enter a postive number")
else:
    original_number=number
    while number>0:
        rem=number%10
        reversed=reversed*10+rem
        number=number//10
    if(original_number==reversed):
            print("Its a Palindrome")
    else:
            print("Its not a Palindrome")
                    