number=int(input("Enter a number :"))
sum=0
temp=number
number_len=len(str(number))
while temp>0:
    rem=temp%10
    sum+=rem**number_len
    temp//=10
if(number==sum):
    print("Armstrong")
else:
    print("Not Armstrong")
