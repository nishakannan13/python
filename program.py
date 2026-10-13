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
                                                                                            
