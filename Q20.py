# Check Given no is Three Digit or Not 
num = int(input("Enter The Number"))
count = 0
temp = abs(num)
while temp!=0:
    last = temp %10
    count = count+1
    temp = temp//10
        
if count == 3:
    print(num, "Number is 3 digit number")
    
else:
    print(num, "Number is Not a 3 digit number")
    
    