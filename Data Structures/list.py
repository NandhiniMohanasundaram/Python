#list possible operation
1.index(ele)
2.pop()
3.del()
4.discard()  //'list' object has no attribute 'discard'
5.remove(ele)
6.clear()
7.extend()
8.append()
9.insert()
10.sort()
11.sorted()
12.copy()
13.count()
14.concat()
15.len(iterables)
16.slice(iterable[start:stop])


my_list=[1,8,6,1,3,2,8,1,9]
print(my_list)
'''
# index(element)-helps to find the position of a particular element over a given lsit
r=my_list.index(8)
print("index: ",r)  //output: index: 1

'''
#pop ---will remove the last element from the list
my_list=[1,3,4,'r','e']
print(my_list.pop())  //output:e
print(my_list)        //output : [1,3,4,'r']



# del lsit[index]-used to delete an element on the specific index
my_list=[1,3,4,'r','e']
del my_list[3]
print(my_list)  //output: [1,3,4,'e']

# remove(element)-allows to remove the particular element at the 1st occurrence on a given list
my_list=[1,3,4,'r','e',3]
my_list.remove(3)
print(my_list)  //output:[1,4,'r','e',3]

#clear()-remove all the element over a given list
c=my_list.clear()
print(c)  //output:[]


'''
 #extend()-is used to add collection of data at the end of existing list
my_list=[1,8,6,1,3,2,8,1,9]
my_list.extend(['a','c'])
print(my_list)  //output: [1,8,6,1,3,2,8,1,9,'a','c']

 #append()-is used to single data at the end of existing list
my_list=[1,8,6,1,3,2,8,1,9]
my_list.append('z')
print(my_list) //output:[1,8,6,1,3,2,8,1,9,'z']
'''
'''
#insert(position,value)-allows you to add new data at the required position over an existing list
my_list=[1,8,6,1,3,2,8,1,9]
my_list.insert(2,'q')
print(my_list) //output:[1, 8, 'q', 6, 1, 3, 2, 8, 1, 9]
'''

'''
#sort() ---will arrange the lsit in the alphabetic order and also arrange number from smaller to higher value
my_list=[1,8,6,1,3,2,8,1,9]
my_list.sort()
print(my_list)  //output:[1, 1, 1, 2, 3, 6, 8, 8, 9]


#sorted(iterables,reverse=True)
my_list=[1,8,6,1,3,2,8,1,9]
print(sorted(my_list,reverse=True))
print(my_list)   //output:[9, 8, 8, 6, 3, 2, 1, 1, 1]
                          [1, 8, 6, 1, 3, 2, 8, 1, 9]

my_list=[1,8,6,1,3,2,8,1,9]
print(sorted(my_list))
print(my_list)        //output:[1, 1, 1, 2, 3, 6, 8, 8, 9]
                                [1, 8, 6, 1, 3, 2, 8, 1, 9]

my_lista=['dam','mon','leg']
my_lista.sort()
print("sort: ",my_lista)  //output:  sort: ['dam', 'leg', 'mon']


mynum=[5,2,1] 
mynum.sort()
print("num",mynum)
# as we can't sort lsit with combination of different data types
# num=[3,'a',4]
# num.sort()
# print(num)      //output: '<' not supported between instances of 'str' and 'int'

#reverse
listz=['a','u']
print(listz)     //output:['a','u']
listz.reverse()
print(listz)     //output:['u','a']

'''

# copy()-duplicate the given list
lists=[1,2,3,'u']
listcopy=lists.copy()
print(lists)             //output:[1, 2, 3, 'u']
print(listcopy)          //output:[1, 2, 3, 'u']



# concat
my_list1=[1,2,3,2]
list2=[12,34,2]
print(my_list1.count(2))
out_tuple=my_list1+list2
print(out_tuple)


# silicing
print(my_list1[0:])
print(my_list1[1:])

#len()
print("length:",len(my_list1))
