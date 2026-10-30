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
n=int(input("Enter a number:"))
count=0
7.prime or not:
for i in range(1,n+1):
    if n%1==0:
        count+=1
if count==2:
    print("Not a Prime")
else:
    print("Prime")
O/P:Enter a number:3
Prime
8.check automorphic number or not:
n=int(input("Enter a number:"))
sq=n*n
if str(sq).endswith(str(n)):
  print("Automorphic number")
else:
  print("Not an Automorphic number")
O/P:
Enter a number:25
Automorphic number
9.check a number is neon number or not:
n=int(input("Enter a number:"))
sq=n*n
s=sum(int(d)for d in str(sq))
if s==n:
  print("Neon number")
else:
  print("Not a neon number")
O/P:Enter a number:1
Neon number
10.check nos is perfect or not:
n=int(input("Enter a number:"))
s=0
for i in range(1,n):
  if n%i==0:
    s+=i
if s==n:
  print("Perfect number")
else:
  print("Not a Perfect number")
O/P:Enter a number:69087
Not a Perfect number
11.Palindrome or not:
n=input("Enter a number:")
if n==n[::-1]:
  print("Palindrome number")
else:
  print("Not a Palindrome")
O/P:Enter a number:7
Palindrome number
12.Duck number:
n=input("Enter a number:")
if '0' in n[1:]:
  print("Duck num")
else:
  print("Not a Duck num")
O/P:Enter a number:1023
Duck num
13.Happy number:
n=int(input("Enter a number:"))
while n!=1 and n!=4:
  sum=0
  while n>0:
    digit=n%10
    sum=sum+digit+digit
    n=n//10
  n=sum
if n==1:
  print("Not a Happy Number")
else:
  print("Happy Number")
O/P:Enter a number:19
Happy Number
14.Peterson number:
n=int(input("Enter a number:"))
temp=n
while n>0:
  digit =n%10
  fact=1
  for i in range(1,digit+1):
    fact=fact+i
    sum = sum
  n = n//10
if sum==temp:
  print(" Not a Peterson Number")
else:
  print("Peterson Number")
O/P:Enter a number:145
Peterson Number
1.num=99
if num>10 and num<100:
  print("Two digit number")
else:
  print("Not a Two digit Number")
O/P:Two digit number
2.num=int(input("Enter a number"))
if num%10==5:
  print("Last digit number is five")
else:
  print("Last digit number is not five")
O/P:Enter a number25
Last digit number is five
3.a=input ("Enter a character")
if a.isalpha():
  print("Alphabet")
elif a.isdigit():
  print("digit")
else:
  print("Special character")
O/P:Enter a character@
Special character
4.a=input("Enter a character:")
if a.isupper():
  print("upperrcase letter")
elif a.islower():
  print("lowercase")
O/P:Enter a character:A
upperrcase letter
5.temp=int(input("enter the temperature:"))
if (temp>37):
  print("temperature is above 37 degree celsius")
elif (temp<37):
  print("tempertaure is below 37 degree celsius")
else:
  print("temperature is 37 degree celsius")
O/P:enter the temperature:38
temperature is above 37 degree celsius
6.bill=int(input("Enter the shopping bill"))
if bill>2000:
  discount=bill*(10/100)
  final_amount = bill-discount
  print("Discount:",discount)
  print("Final amount:",final_amount)
else:
  print("No discount")
  print("Final amount:",bill)
O/P:Enter the shopping bill5000
Discount: 500.0
Final amount: 4500.0
6.month=(input("Enter a Month:"))
if month in("january","march","may"):
  print("Month has 31 days")
elif month in ("april","june","september","november"):
  print("Month has 30 days")
else:
  print("February")
O/P:Enter a Month:january
Month has 31 days
8.marks=float(input("Enter a marks percentage:"))
attendance=float(input("Enter a attendance percentage"))
if marks>=90 and attendance>=85:
  print("Student is eligible for scholarship")
else:
  print("Student is not eligible for scholarship")
O/P:Enter a marks percentage:96
Enter a attendance percentage87
Student is eligible for scholarship
9.num =int(input("Enter a number:"))
last_digit=num%10
print(last_digit)
O/P:Enter a number:4567
7
10.num=int(input("Enter a two digit number:"))
first_digit=num//10
last_digit=num%10
sum=first_digit+last_digit
print(sum)
O/P:Enter a two digit number:47
11
11.a=int(input("Enter a first number:"))
b=int(input("Enter a second number:"))
a,b=b,a
print("After swapping:",a,b)
O/P:Enter a first number:10
Enter a second number:20
After swapping: 20 10
                                                                                            
