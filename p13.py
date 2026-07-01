def count(s):
    str="aeiouAEIOU"
    v=0
    cn=0
    for ch in s:
        if ch in str:
            v+=1
        else:
            cn+=1
    print("vowel", v )
    print("consonant",cn)
count("saurabh")

