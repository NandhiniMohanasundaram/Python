number1=int(input("Enter a number :"))
number2=int(input("Enter a number :"))
# min_val=min(number1,number2)
# for i in range(1,min_val+1):
#     if(number1%i==0 and number2%i==0):
#         gcd=i
# lcm=(number1*number2)/gcd
# print(gcd)
# print(lcm)

    
       
       
       
       
while number2!=0:
     
    r=number1%number2
    number1=number2
    number2=r
gcd=number1
lcm=(number1*number2)//gcd
    


print("gcd",gcd)
print("lcm",lcm)