# question 1 Write a python script to check whether a given number is positive or non-positive

a = int(input("enter your number"))
if a>0:
    print("positive")
if a<=0:
    print("non positive")    

# question 2 Write a python script to check whether a given number is divisible by 5 or not

a = int(input("enter your number"))
if a%5==0:
    print("divisible by 5")
else:
    print("not divisible by 5")

# question 3 Write a python script to check whether a given number is even or odd

a = int(input("enter your number"))
if a%2==0:
    print("number is even")
else:
    print("number is odd")

# question 4 Write a python script to print greater between two numbers. Print number only once even if the numbers are the same.

a = int(input("enter a number"))

b = int(input("enter a number"))

if a>b:
    print ("a is greater than b")
else:
    print(b)
print()

# question 5 Write a python script to print two given words in dictionary order

a = input("enter a word")

b = input("enter a word")

if a>b:
    print(b,a)
else:
    print(a,b)

# question 6 Write a python script to check whether a given number is a three digit number or not.

a = int(input("enter three digit number"))

if 99<a<1000:
    print(a)
else:
    print("invalid")

# question 7 Write a python script to check whether a given number is positive, negative or zero.

a = int(input("enter number"))

if a>0:
    print("positive")
elif a<0:
    print("negative")

else:
    a==0
    print("zero")

# question 8 Write a python script to check whether a given quadratic equation has two real &distinct roots, real & equal roots or imaginary roots

print("enter vale of a,b,and c of a quadratic equation")
a,b,c=int(input()),int(input()),int(input())
d=b**2-4*a*c
if d>0:
    print("Real and distinct roots")
elif d==0:
    print("Real and equal root")
else:
    print("Imaginary roots")

# question 9 Write a python script to check whether a given year is a leap year or not.

year=int(input("enter year"))
if year%400==0 or year%100!=0 and year%4==0:
    print("leap year")
else:
    print("non leap year")


# question 10 Write a python script to print greater among three numbers. Print number only once even if the numbers are the same.

print("enter three number a,b,and c ")
a,b,c=int(input()),int(input()),int(input())
if b<a>c:
    print("a is greater than b and c")
elif a<b>c:
    print("b is greater than a and c")
else:
    print ("c is greater than a and b",c)

# question 11 Write a python script to take the month value in numeric format and display the number of days in it.

month = int(input("enter your number"))
if month in (1,3,5,7,8,10,12):
    print ("31 days")
elif month in (4,6,9,11):
    print("30 days")
elif month==2:
    print("28 or 29 days")
else:
    print("invalid month number")

# question 12

x=complex(input("enter a complex number"))
print(x.real) if x.real>x.imag else print(x.imag)
