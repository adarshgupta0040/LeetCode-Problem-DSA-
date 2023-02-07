class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        temp=""
        ans=[]
        p="".join(sorted(p))
        ind=0
        for i in s:
            temp+=i
            if len(temp)==len(p):
                if "".join(sorted(temp))==p:
                    ans.append(ind)
                ind+=1
                temp=temp[1:]
        return ans
