text=input("Enter a string:")
vowels="aeiouAEIOU"
consonants="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
V=0
C=0
for i in text:
    if i in vowels:
        V+=1
    if i in consonants:
        C+=1
print("vowels:",V)
print("consonants:",C)
