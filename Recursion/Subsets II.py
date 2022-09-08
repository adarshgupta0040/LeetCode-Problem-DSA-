class Solution:
    def f(self,ind,nums,ans,l):
        ans.append(l[:])
        for i in range(ind,len(nums)):
            if i!=ind and nums[i]==nums[i-1]:
                continue
            l.append(nums[i])
            self.f(i+1,nums,ans,l)
            l.pop()
        
            
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        l=[]
        nums.sort()
        self.f(0,nums,ans,l)
        return ans
