class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        incrementCount = 0
        nextNumber = nums[0]
        for i in range(len(nums)):
            if nums[i] < nextNumber:
                incrementCount += nextNumber - nums[i]
            else:
                nextNumber = nums[i]
            nextNumber += 1
        return incrementCount
