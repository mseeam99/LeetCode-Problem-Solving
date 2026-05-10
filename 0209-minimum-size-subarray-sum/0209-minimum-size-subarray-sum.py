class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        leftPointer = 0
        rightPointer = 0

        currentSum = 0
        minLength = float("inf")

        while rightPointer <= len(nums)-1:

            currentSum += nums[rightPointer]

            while currentSum >= target:
                minLength = min(minLength, rightPointer-leftPointer+1)
                currentSum -= nums[leftPointer]
                leftPointer += 1
                
            rightPointer += 1

        if minLength == float("inf"):
            return 0

        return minLength