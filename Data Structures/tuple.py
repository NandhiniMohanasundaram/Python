#tuple possible operation
1.index(ele)
2.count()
3.concat()
4.len(iterables)
5.slice(iterable[start:stop])
6.comparsion


my_tuple1=(1,2,4,9,1)
my_tuple2=('r',4,'y')
print(my_tuple2)

'''
# index(value_to _find its index)
print(my_tuple2.index(4))

# count()
my_tuple1=(1,2,4,9,1)

print(my_tuple1.count(1))

# concat()
my_tuple1=(1,2,4,9,1)
a=(2,3)
print(my_tuple1+a)
# len()
print(len(a))


# silicing
print(my_tuple1[0:])
print(my_tuple1[1:])

print(my_tuple1[0:4])

print(my_tuple1[0:3])


print(my_tuple1[:3])

print(my_tuple1[::])

print(my_tuple1[::-1])    #reversing a tuple

my_tuple1=(1,2,4,9,1)
a=(2,3)
print(my_tuple1>a)       //output:False
'''



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




