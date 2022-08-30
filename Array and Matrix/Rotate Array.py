class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        temp=[0]*n
        for i in range(len(nums)):
            temp[(i+k)%n]=nums[i]
        for i in range(len(nums)):
            nums[i] = temp[i]
