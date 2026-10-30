a=input("Enter a string:")
count=0
consonants=0
for ch in a:
    if ch.isalpha():
         if ch in "aeiouAEIOU":
            count+=1
         else:
            consonants+=1
print("vowels=",count)
print("consonants=",consonants)
