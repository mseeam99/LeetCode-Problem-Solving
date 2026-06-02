class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:

        nums.sort()
        print(nums)

        incrementCount = 0
        nextAvailable = nums[0]

        for i in range(len(nums)):

            if nums[i] < nextAvailable:
                incrementCount += nextAvailable - nums[i]
            else:
                nextAvailable = nums[i]

            nextAvailable += 1

        return incrementCount