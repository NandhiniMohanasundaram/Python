#set possible operation

my_set1={'b',1,4,3,'v'}
my_set2={'r',4,'y'}
print(my_set1)

#extend()  ----------as set are unchangeable and hence it does not have extend operation
# my_set1.extend(my_set2)
# print("hi",my_set1)

#append() ----------as set are unchangeable and hence it does not have append operation
# my_set1.append('sam')
# print(my_set1)

#insert(position,value)----------as set are unchangeable and hence it does not have insert operation
# my_set1.insert(1,"ani")
# print(my_set1)

#pop ---will remove the random element from the set
my_set={1,3,4,'r','e'}
print(type(my_set))
my_set.pop()
print(my_set)

my_sete={1,3,4,'r'}
my_sete.pop()
print('e',my_sete)


# remove(value to be removed)     ---if there is given value among the set element then it will be removed else throws error
print('r is removed ',my_set.remove(3))
print(my_set)

# discard()   -----it act same as the remove().
# The key difference is that in remove() the given value is not present it will throw error whereas discard dosn't do that

# add()
my_set.add(8)
print(my_set)
#sort() ----------as set are unchangeable and hence it does not have sort operation
# my_seta={'dam','mon','leg'}
# my_seta.sort()
# print("sort",my_seta)

# mynum={5,2,1}
# mynum.sort()
# print("num",mynum)

# num={3,'a',4}
# num.sort()
# print(num)

#reverse ----------as set are unchangeable and hence it does not have extend operation
# print(my_set)
# my_set.reverse()
# print(my_set)

