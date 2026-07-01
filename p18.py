def simple(p,r,t):
    sum1=(p*r*t)/100
    return sum1
def ci(p,r,t):
    sum2=p* ((1 + r/100) ** t) - p
    return sum2
print(simple(2000,5,1))
print(ci(2000,5,1))