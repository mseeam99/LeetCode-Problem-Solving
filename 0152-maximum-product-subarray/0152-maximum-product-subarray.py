class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        result = max(nums)

        curMax, curMin = 1, 1

        for i in range(len(nums)):
            currentValue = curMax * nums[i]  
            curMax = max(nums[i], currentValue, curMin * nums[i])
            curMin = min(nums[i], currentValue, curMin * nums[i])
            result = max(result, curMax)
            print("CURMAX: ",curMax, " CURMIN: ", curMin, " RESULT: ", result)
        return result
