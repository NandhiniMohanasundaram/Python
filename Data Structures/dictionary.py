# #dict possible operation
1.pop(key)
2.del()
3.clear()
4.len(iterables)

# my_dict1={1:'apple',2:"orange",3:"mango"}
# my_dict2={'name1':"anu","name2":"priya","name3":"zara"}
# print(my_dict2)
'''
# pop()
my_dict2={'name1':"anu","name2":"priya","name3":"zara"}
print(my_dict2.pop("name1"))  output:anu

my_dict2={'name1':"anu","name2":"priya","name3":"zara"}
del my_dict2["name1"]
print(my_dict2)      //output:{'name2': 'priya', 'name3': 'zara'}


# clear()
my_dict2={'name1':"anu","name2":"priya","name3":"zara"}
my_dict2.clear()
print(my_dict2)

# copy
my_dict2={'name1':"anu","name2":"priya","name3":"zara"}
r=my_dict2.copy()
# print(my_dict2)         output: {'name1': 'anu', 'name2': 'priya', 'name3': 'zara'}


# len()
my_dict2={'name1':"anu","name2":"priya","name3":"zara"}
s=len(my_dict2)
print(s)
'''

# # index(value_to _find its index) -------dict is accessed by key ,thereby index is not available in dictionary
# # print(my_dict2.index(2))

# # silicing
# print(my_dict1[1:])
# print(my_dict1[1:])

# print(my_dict1[0:4])

# print(my_dict1[0:3])


# print(my_dict1[:3])

# print(my_dict1[::])

# print(my_dict1[::-1])    #reversing a dict

# # concat
# out_dict=my_dict1+my_dict2
# print(out_dict)

# #len()
# print("length:",len(my_dict1))

#count(value to be count)
# print(my_dict1.count(1))



#extend() ----its an mutable operation and hence can't be performed with dict
# my_dict1.extend(my_dict2)
# print("hi",my_dict1)

# #append() ----its an mutable operation and hence can't be performed with dict
# my_dict1.append('sam')
# print(my_dict1)

# #insert(position,value) ----its an mutable operation and hence can't be performed with dict
# my_dict1.insert(1,"ani")
# print(my_dict1)

#pop ----its an mutable operation and hence can't be performed with dict
# my_dict=(1,3,4,'r','e')
# my_dict.pop()
# print(my_dict)

# my_dicte=(1,3,4,'r')
# my_dicte.pop()
# print('e',my_dicte)

#sort() ----its an mutable operation and hence can't be performed with dict
# my_dicta=('dam','mon','leg')
# my_dicta.sort()
# print("sort",my_dicta)

# mynum=(5,2,1)
# mynum.sort()
# print("num",mynum)

# num=(3,'a',4)
# num.sort()
# print(num)

#reverse ----its an mutable operation and hence can't be performed with dict
# print(my_dict)
# my_dict.reverse()
# print(my_dict)




set1={1,3,4}
print(type(set1))
