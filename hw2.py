jewels=input("Enter a jewels:")
stones=input("Enter a stones:")
count=0
for i in stones:
    if i in jewels:
        count+=1
print(count)
        
