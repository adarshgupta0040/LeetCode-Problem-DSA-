class Solution:
    def f(self,ind,summ,arr,n,ans):
        if ind==n:
            ans.append(summ)
            return
        self.f(ind+1,summ+arr[ind],arr,n,ans)
        self.f(ind+1,summ,arr,n,ans)
	def subsetSums(self, arr, N):
	    ans=[]
	    self.f(0,0,arr,N,ans)
	    ans.sort()
	    return ans
