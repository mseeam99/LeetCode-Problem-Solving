class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = {}

        def recursion(index, current):
            if index == len(nums):
                if current == target:
                    return 1 
                else:
                    return 0

            if (index, current) in memo:
                return memo[(index, current)]

            add = recursion(index + 1, current + nums[index])
            subtract = recursion(index + 1, current - nums[index])

            memo[(index, current)] = add + subtract
            return memo[(index, current)]

        return recursion(0, 0)
