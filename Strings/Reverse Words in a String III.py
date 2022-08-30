class Solution:
    def reverseWords(self, s: str) -> str:
        a=s[::-1]
        ans=""
        l=a.split(" ")
        print(l)
        for i in range(len(l)):
            ans+=l[i][::-1]
            if i!=len(l)-1:
                ans+=" "
        return ans[::-1]
