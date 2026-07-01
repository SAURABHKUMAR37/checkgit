data=int(input("enter number of 6 digit"))
a=data//100000
data=data%100000

b=data//10000
data=data%10000

c=data//1000
data=data%1000

d=data//100
data=data%100

e=data//10
data=data%10

f=data%10
lockn=a+b+c

seck=d*100+e*10+f
if(seck%lockn==0):
    print("grant acess")
else:
    print("denied")