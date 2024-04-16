number=int(input("Enter a number to be reversed: "))
reversed=0
temp=number
while(temp!=0):
    remainder=temp%10
    reversed=reversed*10+remainder
    temp=temp//10
print("Reversed Number:",reversed)
if(number==reversed):
    print("palindrome")
else:
    print("not palindrome")
