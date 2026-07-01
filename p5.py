a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
if(a>b and a>c):
    print("a is greater")
elif(b>c and b>a):
    print("b is greater")
else:
    print("c is greater")
if(a<b and a<c):
    print("a is smallest")
elif(b<c and b<a):
    print("b is smallest")
else:
    print("c is smallest")