class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans=""
        for i in range(len(s)):
            if s[i].isalnum():
                ans+=s[i].lower()
        if ans==ans[::-1]:
            return True
        
