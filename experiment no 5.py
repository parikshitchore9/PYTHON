#question number 1
a="parikshit"
print(len(a))

#question number 2
b=input("enter the string:")
if len(b)<2:
    print("the length of string is too short:")
c=b[:2]
d=b[-2:]
result=c+d
print("the string made by first and last two character of the given string is",c+d)

#question number 3
e=input("enter the first string:")
f=input("enter the second string:")

print("concatenate=",e+f)