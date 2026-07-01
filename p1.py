data=(input("enter  4 digit number"))
# a=data//1000
# data=data%1000

# b=data//100
# data=data%100

# c=data//10
# data=data%10


# d=data%10

a=data[0]
b=data[1]
c=data[2]
d=data[3]
print(a,b,c,d)
pa="5432"
if(pa[0]==a  and pa[1]==b and pa[2]==c and pa[3]==d):
    print("exact matching")
elif(pa[0]==a and pa[1]==b):
    print("partially correct")
else:
    print(" nopt matching")
