class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort() #Sort the array
        answer = nums[0] + nums[1] + nums[2] #initialise Answer
        n=len(nums)
        for i in range(n-2):
            j=i+1 #take 2 ptr
            k=n-1
            while(j<k):
                sum=nums[i]+nums[j]+nums[k] # count sum 
                if sum < target:  #if sum too small , inc j ptr
                    j=j+1
                elif sum > target:  #if sum too large, dec k ptr
                    k=k-1
                else:  #if sum == target 
                    return sum
                if abs(sum - target) < abs(answer - target):
                    answer = sum
        return answer
      
      
# Approch 2:


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float('inf')
        for i in range(len(nums) - 2):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                s = nums[i] + nums[lo] + nums[hi]
                if s == target:
                    return s
                elif s > target:
                    hi -= 1
                else:
                    lo += 1
                if abs(s - target) < abs(ans - target):
                    ans = s
        return ans
