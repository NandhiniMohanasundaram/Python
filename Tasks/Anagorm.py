# slient==listen
# horse==shore
# small==malls
_string1=input("Enter a first string:")
_string2=input("Enter a second string:")
_string1_low=_string1.lower()
_string2_low=_string2.lower()
if(len(_string1_low)==len(_string2_low) and sorted(_string1_low)==sorted(_string2_low)):
    print("Anagorm")
else:
    print("Not a Anogorm")