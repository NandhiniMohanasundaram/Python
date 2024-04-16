#tuple possible operation

my_tuple1=(1,2,4,9,1)
my_tuple2=('r',4,'y')
print(my_tuple2)


# index(value_to _find its index)
print(my_tuple2.index(4))

# silicing
print(my_tuple1[0:])
print(my_tuple1[1:])

print(my_tuple1[0:4])

print(my_tuple1[0:3])


print(my_tuple1[:3])

print(my_tuple1[::])

print(my_tuple1[::-1])    #reversing a tuple

# concat
out_tuple=my_tuple1+my_tuple2
print(out_tuple)

#len()
print("length:",len(my_tuple1))

#count(value to be count)
print(my_tuple1.count(1))



#extend() ----its an mutable operation and hence can't be performed with tuple
# my_tuple1.extend(my_tuple2)
# print("hi",my_tuple1)

# #append() ----its an mutable operation and hence can't be performed with tuple
# my_tuple1.append('sam')
# print(my_tuple1)

# #insert(position,value) ----its an mutable operation and hence can't be performed with tuple
# my_tuple1.insert(1,"ani")
# print(my_tuple1)

#pop ----its an mutable operation and hence can't be performed with tuple
# my_tuple=(1,3,4,'r','e')
# my_tuple.pop()
# print(my_tuple)

# my_tuplee=(1,3,4,'r')
# my_tuplee.pop()
# print('e',my_tuplee)

#sort() ----its an mutable operation and hence can't be performed with tuple
# my_tuplea=('dam','mon','leg')
# my_tuplea.sort()
# print("sort",my_tuplea)

# mynum=(5,2,1)
# mynum.sort()
# print("num",mynum)

# num=(3,'a',4)
# num.sort()
# print(num)

# reverse ----its an mutable operation and hence can't be performed with tuple
rmy_tuple=(3,'d',5)
rmy_tuple.reverse()
print(rmy_tuple)




