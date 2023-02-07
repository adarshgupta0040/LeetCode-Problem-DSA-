class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        l1=len(s1)
        l2=len(s2)
        s1="".join(sorted(s1))
        # print(s1)
        for i in range(l2-l1+1):
            temp=s2[i:l1+i]
            temp="".join(sorted(temp))
            if temp==s1:
                return True
        return False
