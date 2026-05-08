class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        leftPointer = 0
        rightPointer = 0

        zeroCount = 0
        oneCount = 0

        maxLength = 0

        while rightPointer <= len(nums)-1:



            if nums[rightPointer] == 1:
                oneCount +=1
            elif nums[rightPointer] == 0:
                zeroCount += 1

            while zeroCount > 1:# zero found
                if nums[leftPointer] == 0:
                    zeroCount -= 1
                leftPointer += 1

            maxLength = max(maxLength,rightPointer-leftPointer+1)

            rightPointer += 1

        
        return maxLength
            





        