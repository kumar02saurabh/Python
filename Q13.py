#LCM of Two Number
num1 = int(input("Enter the Number1"))
num2 = int(input("Enter the Number2"))
max_num = max(num1,num2)
while True:
    if max_num % num1 ==0 and max_num % num2 ==0:
        print("LCM of",num1, "and" ,num2, "is",max_num)
        break
    max_num+=1