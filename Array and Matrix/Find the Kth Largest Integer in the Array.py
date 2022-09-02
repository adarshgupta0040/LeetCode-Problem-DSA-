class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        a=[int(nums[x]) for x in range(len(nums))]
        a.sort()
        return str(a[-k])
