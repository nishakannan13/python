num=[0,1,0,3,12]
for i in range(len(num)):
    if num[i]==0:
        num.append(num[i])
        num.remove(num[i])
print(num)


