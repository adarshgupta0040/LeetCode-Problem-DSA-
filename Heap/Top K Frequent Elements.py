class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        maxheap=[]
        ans=[]
        for key,val in d.items():
            heapq.heappush(maxheap,[-val,key])
            
        # print(minheap)
        
        for i in range(k):
            val,key=heapq.heappop(maxheap)
            ans.append(key)
        return ans
