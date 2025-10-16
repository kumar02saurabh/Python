#Check Number is prime or not
num = int(input("Enter The Number"))
flag = 0
if num <2:
    print("Given Number is not prime")
else:
    for i in range (2,num//2+1):
        if num%2==0:
            flag = 1
            print("Given Number is not prime")
            break
    if flag == 0:
        print("Given Number is Prime")
    
        
        
