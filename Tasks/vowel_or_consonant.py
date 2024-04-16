# input_string=input("Enter a character: ")
# input_string=input_string.lower()
# vowel=['a','e','i','o','u']
# if(input_string in vowel):
#     print("It is a vowel")
# elif(input_string not in vowel):
#     print("It is a consonant")
# else:
#     print("Enter a valid character")

input_string=input("Enter a string: ")
input_string=input_string.lower()
vowel=['a','e','i','o','u']
vowel_count=0
const_count=0
vowels=[]
cons=[]
for i in input_string:
    if (i in vowel):
        vowels.append(i)
        vowel_count=vowel_count+1
    elif (i not in vowel):
        cons.append(i)
        const_count=const_count+1


if(vowel_count>1 and const_count>1):
    print("The number of vowels in the given string is :",vowel_count)
    print("Vowels in the given string",vowels)
    print("The number of consonant in the given string is :",const_count)
    print("Consonant in the given string",cons)
else:
    print("Re-enter a proper string")
        

