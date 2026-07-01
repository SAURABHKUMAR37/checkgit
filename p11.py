def check(s):
    freq={}
    count=[]
    for ch in s:
        freq[ch]=freq.get(ch,0)+1
        count.append(freq[ch])
    return count
def c(s1,s2):
    if(check(s1)==check(s2)):
        return True
    else:
        return False
print(c("egg","adp"))