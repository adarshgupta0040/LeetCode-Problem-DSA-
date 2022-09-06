class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        ans = []
        for i in range(len(nums)):
            ans.append(heapq.heappop(nums))
        return ans
