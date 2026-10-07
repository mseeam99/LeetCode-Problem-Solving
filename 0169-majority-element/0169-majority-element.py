class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        '''
        nums.sort()
        majorityCount = 0
        majorityVal = 0
        leftPointer = 0
        rightPointer = 0
        while rightPointer <= len(nums)-1:
            if nums[leftPointer] == nums[rightPointer]:
                rightPointer += 1
            else:
                if rightPointer-leftPointer > majorityCount:
                    majorityCount = max(majorityCount,rightPointer-leftPointer)
                    majorityVal = nums[leftPointer]
                leftPointer = rightPointer
        if rightPointer-leftPointer > majorityCount:
            majorityCount = max(majorityCount,rightPointer-leftPointer)
            majorityVal = nums[leftPointer]
        return majorityVal
        '''
        previousValue = 0
        count = 0
        for i in range(len(nums)):
            if count == 0:
                previousValue = nums[i]
            element = nums[i]
            if nums[i] == previousValue:
                count += 1
            elif nums[i] != previousValue:
                count -= 1
        return previousValue






       

        
        