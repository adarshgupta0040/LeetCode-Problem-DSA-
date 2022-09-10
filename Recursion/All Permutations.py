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

    
    
# Approch 2

class Solution:
    def f(self,ind,arr,ans):
        if ind==len(arr):
            ds=[]
            for i in range(len(arr)):
                ds.append(arr[i])
            ans.append(ds[:])
            return 
        for i in range(ind,len(arr)):
            arr[i],arr[ind]=arr[ind],arr[i]
            self.f(ind+1,arr,ans)
            arr[i],arr[ind]=arr[ind],arr[i]
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        self.f(0,nums,ans)
        return ans
    
    
