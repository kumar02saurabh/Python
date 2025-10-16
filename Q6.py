#find Unicode for each char in given string and also find sum
text = input("Enter The String: ")
sum = 0
for ch in text:
    print(f"{ch}: {ord(ch)}")
    sum = sum+ord(ch)


print("Sum Of each Unicode in a Given String is :",sum)

