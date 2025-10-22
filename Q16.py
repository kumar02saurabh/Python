#Remove The Last Digit From The Given Number 
num = int(input("Enter The Number:"))
last = num % 10
print("Last digit of the number is",last)
num = num //10
print("New Number is",num)
