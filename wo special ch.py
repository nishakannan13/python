a=input("Enter a string:")
for i in a:
    if i.isalnum():
        if i.islower():
            print(i.upper(),end="")
for j in a:
    if j.isalnum():
        if j.isupper():
            print(j.lower(),end="")
