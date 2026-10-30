a=input("Enter a string:")
count=0
vowels="aeiouAEIOU"
for i in a.split():
    if i[0] in vowels:
        count+=1
print("Words starts with vowels:",count)
    
