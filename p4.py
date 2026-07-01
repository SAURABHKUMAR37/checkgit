a=int(input("enter 1 side"))
b=int(input("enter 2 side"))
c=int(input("enter 3 side"))
if(a+b>c or b+c>a or a+c>b):
    print("valid")
    if(a==b==c):
        print("equilateral triangle")
    elif(a==b or b==c or a==c):
        print("isolses triangle")
    else:
        print("scalen triangle")

else:
    print("not valid")

