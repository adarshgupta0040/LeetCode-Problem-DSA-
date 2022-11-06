class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k==1:
            n=len(s)
            doublestr=s+s
            ans=s
            for i in range(1,n):
                s1=doublestr[i:n+i]
                print(s1)
                if s1<ans:
                    ans=s1
            return ans
        else:
            res = ''.join(sorted(s))
            return res
