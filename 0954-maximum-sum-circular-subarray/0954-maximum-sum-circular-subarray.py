class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        globalMax,globalMin = nums[0],nums[0]
        currentMax,currentMin = 0,0
        total = 0

        for num in nums:

            currentMax = max(num,currentMax+num)
            globalMax = max(globalMax,currentMax)

            currentMin = min(num,currentMin+num)
            globalMin = min(globalMin,currentMin)

            total += num

        if total == globalMin:
            return globalMax

        return max(globalMax,total - globalMin)




       
        