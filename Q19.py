#Check Two words are in Dictionary Order or Not
word1 = input("Enter The first word")
word2 = input("Enter The second word")
w1 = word1.lower()
w2 = word2.lower()

if w1 > w2:
    print(word1," comes Before", word2)
elif w1<w2:
    print(word2," comes After", word1)
else:
    print("Both Words are equal")