# Swap data  
num1 = int(input("Enter the value1:"))
num2 = int(input("Enter the value2:"))
num2,num1 = num1,num2
print("After Swapping num1 is :",num1)
print("After Swapping num2 is :",num2)


#method 2
print("Method 2-------------------")
num1 = int(input("Enter the value1:"))
num2 = int(input("Enter the value2:"))
temp = num1
num1 = num2
num2 = temp

print("After Swapping num1 is :",num1)
print("After Swapping num2 is :",num2)

#Method 3 
print("Method 3-------------------")
num1 = int(input("Enter the value1:"))
num2 = int(input("Enter the value2:"))

num1 = num1+num2
num2 = num1-num2
num1 = num1-num2

print("After Swapping num1 is :",num1)
print("After Swapping num2 is :",num2)


#Method 4
print("Method 4-------------------")
num1 = int(input("Enter the value1:"))
num2 = int(input("Enter the value2:"))

num1 = num1^num2
num2 = num1^num2
num1 = num1^num2

print("After Swapping num1 is :",num1)
print("After Swapping num2 is :",num2)