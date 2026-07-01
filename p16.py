a=int(input(" enter first number"))
b=int(input(" enter second number"))
c=int(input(" enter third number"))
def check(a,b,c):
    if(a<b and a<c):
        print(" a is smallest")
    if(b<a and b< c):
        print(" b is smallest")
    else:
        print(" c is smallest ")
check(a,b,c)

