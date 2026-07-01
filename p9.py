# def rec(num):
#     if(num==0 or num==1):
#         return num
#     else:
#         return rec(num-1)+rec(num-2)
# print(rec(4))
def rec(num):
    a,b=0,1
    for i in range(num):
        a,b=b,a+b
    return a
print(rec(4))