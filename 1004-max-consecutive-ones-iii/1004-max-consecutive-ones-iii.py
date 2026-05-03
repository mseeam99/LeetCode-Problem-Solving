class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        leftPointer  = 0
        rightPointer = 0

        maxLength = 0
        zeroCount = 0

        while rightPointer <= len(nums)-1:

            if nums[rightPointer] == 1:
                rightPointer += 1
            elif nums[rightPointer] == 0 and zeroCount <= k:
                zeroCount += 1
                rightPointer += 1

            while zeroCount > k:
                if nums[leftPointer] == 0:
                    zeroCount -= 1
                leftPointer += 1
           
            maxLength = max(maxLength, rightPointer-leftPointer + 1)

        return maxLength-1
