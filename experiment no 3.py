  # first question
a=input("enter the first number:")
b=input("enter the second number:")
c=input("enter the third number:")
 
if a>b and a>c :
    print("a is greatest",a)

elif b>c and b>a:
    print("b is greatest",b)

else :
    print("c is greatest",c)

#second question
num=int(input("enter the nummber:"))
if num%2==0:
    print("the num is even :",num)
else:
    print("the num is odd:",num)

#third question
value=(input("enter the input:"))
if value.isdigit:
    print("the input value is digit:",value)
elif value.isalpha:
    print("the input value is alphabet:",value)
else:
    print("the input value is special character:",value)   