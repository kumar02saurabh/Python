#Check Given Year is leap year or Not
year = int(input("Enter The Year:"))
if year >0:
    if (year % 4==0 and year %100!=0) or (year %400 ==0):
        print("Given Year is Leap year")
    else:
        print("Not a leap year")
else: 
    print("Year is Not Valid")
