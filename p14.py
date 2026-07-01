def prime(num):
    c=0
    for i in range(2,num):
        if(num%i==0):
            c+=1
    if(c==0):
        return num
def get( nums):
    for i in range(2,nums+1):
        print(prime(i))
get(5)
    
