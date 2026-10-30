a=input("Enter a string:")
b=input("Enter a string:")
ch_a={}
ch_b={}
for i in a.lower():
    if i in ch_a:
        ch[i]+=1
    else:
        ch_a[i]=1
for i in b.lower():
    if i in ch_b:
        ch_b[i]=1
    else:
        ch_b[i]=1
if ch_a==ch_b:
    print("Anagram")
else:
    print("Not an Anagram")
