class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        total   = nums[0]
        for i in range(1,len(nums)):
            current = max(nums[i],current+nums[i])
            total   = max(total,current)
        return total
        