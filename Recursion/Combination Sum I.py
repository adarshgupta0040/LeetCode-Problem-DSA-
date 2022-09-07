class Solution:
    def f(self,ind,k,arr,l,ans,n):
        if ind==n:
            if k==0:
                ans.append(l[:])
            return
        if k<0:
            return 
        if arr[ind]<=k:
            l.append(arr[ind])
            self.f(ind,k-arr[ind],arr,l,ans,n)
            l.pop()
        self.f(ind+1,k,arr,l,ans,n)
        
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        ans=[]
        self.f(0,target,nums,[],ans,n)
        return ans
