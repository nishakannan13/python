a=input("Enter a string:")
for ch in a:
    if a.count(ch)==1:
        print("First non repeating character:",ch)
        break
