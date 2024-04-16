#list possible operation

my_list1=['b',1,4,3,'v','b']
my_list2=['r',4,'y']
# print(my_list1)
'''
# #extend()-is used to add collection of data at the end of existing list
# my_list1.extend(my_list2)
# print("hi",my_list1)

# #append()-is used to single data at the end of existing list
# my_list1.append('sam')
# print(my_list1)
'''
'''
# index(element)-helps to find the position of a particular element over a given lsit
print('gggggggg',my_list1)
r=my_list1.index(4)
print("index",r)


#insert(position,value)-allows you to add new data at the required position over an existing list
my_list1.insert(1,"ani")
print(my_list1)
'''
'''
# remove(element)-allows to remove the particular element at the 1st position on a given list
print(my_list1)
my_list1.remove('b')
print(my_list1)

#pop ---will remove the last element from the list
my_list=[1,3,4,'r','e']
my_list.pop()
print(my_list)
'''
'''
my_liste=[1,3,4,'r']
my_liste.pop()
print('e',my_liste)

c=my_liste.clear()
print(c)
'''
'''
#sort() ---will arrange the lsit in the alphabetic order and also arrange number from smaller to higher value
my_lista=['dam','mon','leg']
my_lista.sort()
print("sort",my_lista)


mynum=[5,2,1] 
mynum.sort()
print("num",mynum)
# as we can't sort lsit with combination of different data types
# num=[3,'a',4]
# num.sort()
# print(num)

#reverse
listz=['a','u']
print(listz)
listz.reverse()
print(listz)

'''

# copy()-duplicate the given list
lists=[1,2,3,'u']
listcopy=lists.copy()
print(lists)
print(listcopy)