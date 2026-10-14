1.count number divisible by 5(range1-50):
num=[10,20,30,35,40,45]
count=0
for num in range(1,51):
  if num%5==0:
    count+=1
print(count)
O/P:10
2.sum of odd numbers|(range1-20):
sum=0
for i in range(1,21):
  if(i%2!=0):
    sum+=i
print(sum) 
O/P:100
3.numbers divisible by  3 but not ny 4(range 1-30):
for i in range(1,31):
  if i%3==0 and i%4!=0:
    print(i)
O/P:3
6
9
15
18
21
27
30
4.count +ve  & -ve nos:
num=[5,6,-9,8,-4]
positive=0
negative=0
for i in num:
 if i>=0:
  positive+=1
 elif i<0:
  negative+=1
print("Positive numbers:",positive)
print("Negative numbers:",negative)
O/P:Positive numbers: 3
Negative numbers: 2
5.largest nums without using max():
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if a>=b and a>=c:
  print("Largest number is",a)
elif b>=a and b>=c:
  print("Largest number is",b)
else:
  print("Largest number is",c)
O/P:Enter first number:90
Enter second number:78
Enter third number:45
Largest number is 90
6.factorial:
n=int(input("Enter a number:"))
fact=1
i=1
while i<=n:
  fact =fact*i
  i+=1
print("Factorial:",fact)
O/P:Enter a number:5
Factorial: 120

