class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxValue = float("-inf")
        memo = {}

        def recursion(index, currentSum):
            nonlocal maxValue, memo
            if index == len(nums):
                return
    
            if (index, currentSum) in memo:
                return memo[(index, currentSum)]
            
            if currentSum < 0:
                currentSum = 0

            currentSum = currentSum + nums[index]
            maxValue = max(maxValue, currentSum)
            
            memo[(index, currentSum)]=recursion(index + 1, currentSum)

        recursion(0, 0)
        return maxValue

        '''
        currentSum = 0
        maxSum = nums[0]
        for i in range(len(nums)):
            if currentSum <= 0:
                currentSum = 0
            currentSum += nums[i]
            maxSum = max(maxSum,currentSum)
        return maxSum
        '''



        