#Count the number of digit
num = int(input("Enter The Number:"))
count = 0
while num>0:
    rem = num % 10
    count = count + 1
    num = num//10
    
print("Total Number of Digit is:",count)
    
