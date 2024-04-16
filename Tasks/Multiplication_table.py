number=int(input("Enter a number :"))
num_range=int(input("Enter a range :"))
print("The factors of ",number,"are")
for i in range(1,num_range+1):
    result=number*i
    print("",number,"*",i,"=",result)