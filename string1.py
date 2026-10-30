a=input("Enter a string:")
vowels="aeiouAEIOU"
for i in a.split():
    if i in vowels:
        i.replace("vowels","*")
print(a)

