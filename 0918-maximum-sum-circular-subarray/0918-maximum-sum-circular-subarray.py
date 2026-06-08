class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        totalSum = sum(nums)

        globalMax = nums[0]
        globalMin = nums[0]
        
        curMax = 0
        curMin = 0

        for i in range(len(nums)):
            curMax = max(curMax+nums[i],nums[i])
            globalMax = max(globalMax,curMax)
            curMin = min(curMin+nums[i],nums[i])
            globalMin = min(globalMin,curMin)

        if globalMax > 0:
            return max(globalMax,totalSum-globalMin)
        else:
            return globalMax
        





        

        