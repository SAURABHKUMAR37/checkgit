data=int(input("enter number"))

while data>=10:
    sum1=0
    while(data>0):
        r=data%10
        data=data//10
        sum1+=r
    data=sum1

print(data)