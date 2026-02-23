class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        currentSum = sum(nums[:k])
        maxValue = sum(nums[:k])

        for i in range(k,len(nums)):
            currentSum += nums[i]
            currentSum -= nums[i-k]
            maxValue = max(maxValue,currentSum)

        return maxValue / k

        

        
        