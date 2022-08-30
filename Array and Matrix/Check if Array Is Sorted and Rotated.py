class Solution:
    def check(self, nums: List[int]) -> bool:
        count=0
        n=len(nums)
        for i in range(1,n):
            if nums[i-1]>nums[i]:
                count+=1
        print(count)
        if nums[n-1]>nums[0]:
            count+=1
        if count<=1:
            return True
        return False
                
