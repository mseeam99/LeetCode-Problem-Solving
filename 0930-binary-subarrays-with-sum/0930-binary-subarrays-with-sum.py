class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def helper(nums,goal):
            if goal < 0:
                return 0
            leftPointer = 0
            rightPointer = 0
            ways = 0
            value = 0
            while rightPointer <= len(nums)-1:
                value += nums[rightPointer]
                while value > goal:
                    value -= nums[leftPointer]
                    leftPointer += 1
                ways = ways + (rightPointer-leftPointer+1)
                rightPointer += 1
            return ways

        return helper(nums,goal)-helper(nums,goal-1)


            



        