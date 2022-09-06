def f(s,ind,curr=""):
    if ind==len(s):
        print(curr)
        return 
    f(s,ind+1,curr+s[ind])
    f(s,ind+1,curr)
    
s=input()
f(s,0,"")
