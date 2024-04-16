year=int(input("Enter a  year:"))
if len(str(year))<4:
    print("Enter a proper year")
elif len(str(year))==4:
    if year%4==0:
        print("Leap year")
    else:
        print("Not a leap year")   