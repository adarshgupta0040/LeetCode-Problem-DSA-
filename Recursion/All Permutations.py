class Solution:
    def f(self,ds,arr,freq,ans):
        if len(ds)==len(arr):
            ans.append(ds[:])
            return 
        for i in range(len(arr)):
            if freq[i]==0:
                ds.append(arr[i])
                freq[i]=1
                self.f(ds,arr,freq,ans)
                freq[i]=0
                ds.pop()
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        freq=[0]*n
        ds=[]
        self.f(ds,nums,freq,ans)
        return ans
