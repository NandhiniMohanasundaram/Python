list1=[1,2,3,8,5,4,8,3,0]
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]==list1[j]:
           print(list1[j])
