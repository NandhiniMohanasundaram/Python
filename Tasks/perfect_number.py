number=int(input("Enter a number :"))
sum=0
print("The factors of ",number,": ")
for i in range(1,number):
    if(number%i==0):
        print(i,end=" ")
        sum+=i
print(sum)
    
if(number==sum):
    print("The given",number,"is perfect number")    
else:
     print("The given",number,"is not a perfect number") 

