class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        nums.sort()

        leftPointer = 0
        rightPointer = 0

        windowSum = 0
        maxLength = 0

        while rightPointer <= len(nums)-1:

            windowSum += nums[rightPointer]

            
            while nums[rightPointer] * (rightPointer-leftPointer+1) - windowSum > k:
                windowSum -= nums[leftPointer]
                leftPointer += 1

        
            maxLength = max(maxLength,(rightPointer-leftPointer+1))
            
            rightPointer += 1

        return maxLength



        