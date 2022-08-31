# Brute Force :

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums.count(nums[i])==1:
                return nums[i]
      
     
# Optimised :

# A^A=0
# A^B^A=B
# (A^A^B) = (B^A^A) = (A^B^A) = B This shows that position doesn't matter.
# Similarly , if we see , a^a^a......... (even times)=0 and a^a^a........(odd times)=a

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            ans=ans^nums[i]
        return ans
