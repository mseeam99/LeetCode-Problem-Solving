class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        answer = float('inf')
        difference = float('inf')
        for i in range(len(nums)):
            leftPointer = i+1
            rightPointer = len(nums)-1
            while leftPointer < rightPointer:
                addedValue = nums[i] + nums[leftPointer] + nums[rightPointer]
                tempDifference = abs(target - addedValue)
                if tempDifference <= difference:
                    answer = addedValue
                    difference = tempDifference 
                if addedValue < target:
                    leftPointer+=1
                elif addedValue > target:
                    rightPointer-=1
                else:
                    return target
        return answer