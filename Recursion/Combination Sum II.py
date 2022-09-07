class Solution:
    def f(self,ind,k,arr,ans,l):
        if k==0:
            ans.append(l[:])
            return 
        for i in range(ind,len(arr)):
            if i>ind and arr[i]==arr[i-1]:  #duplicate
                continue
            if arr[ind]>k:
                break
            l.append(arr[i])
            print(l)
            self.f(i+1,k-arr[i],arr,ans,l)
            l.pop()
        
            
    def combinationSum2(self, arr: List[int], target: int) -> List[List[int]]:
        arr.sort()
        ans=[]
        l=[]
        self.f(0,target,arr,ans,l)
        return ans
