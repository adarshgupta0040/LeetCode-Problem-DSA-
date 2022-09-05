# Brute Force 
def findKthLargest(self, nums: List[int], k: int) -> int:
    nums.sort()
    l=len(nums)
    return nums[l-k]

  
  
# OPTIMISED :

def findKthLargest(self, nums: List[int], k: int) -> int:
    minheap=[]
    for i in nums:
        heappush(minheap,i)
        if len(minheap)>k:
            heappop(minheap)
    return minheap[0]
