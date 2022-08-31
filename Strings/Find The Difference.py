class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d={}
        for i in t:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in s:
            if i in d:
                d[i]-=1
            else:
                d[i]=1
        print(d)
        for k,v in d.items():
            if v==1:
                return k
