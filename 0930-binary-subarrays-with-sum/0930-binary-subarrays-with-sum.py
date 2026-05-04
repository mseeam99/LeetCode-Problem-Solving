class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def helper(goal):
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
                ways += (rightPointer-leftPointer+1)
                rightPointer += 1
            return ways

        return helper(goal)-helper(goal-1)


            



        