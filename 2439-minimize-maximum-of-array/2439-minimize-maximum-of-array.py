class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        result = nums[0]
        totalSum = nums[0]
        for i in range(1,len(nums)):
            totalSum += nums[i]
            result = max(result, ceil(totalSum/(i+1)))
        return result