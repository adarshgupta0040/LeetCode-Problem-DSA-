class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        leftmax=0
        rightmax=0
        ans=0
        while(l<r):
            if height[l]<height[r]:
                if height[l]>leftmax:
                    leftmax=height[l]
                else:
                    ans+=leftmax-height[l]
                l+=1
            else:
                if height[r]>rightmax:
                    rightmax=height[r]
                else:
                    ans+=rightmax-height[r]
                r-=1
        return ans 
