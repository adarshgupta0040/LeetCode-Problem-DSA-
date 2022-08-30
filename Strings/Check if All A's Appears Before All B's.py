class Solution:
    def checkString(self, s: str) -> bool:
        s1=sorted(s)
        if s=="".join(s1):
            return True
        return False
