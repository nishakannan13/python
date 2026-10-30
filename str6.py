a=input("Enter a string:")
for ch in set(a):
    count=0
    if a.count(ch)>1:
          print(ch)

