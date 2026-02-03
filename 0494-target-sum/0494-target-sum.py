class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = {}

        def recursion(index,currentSum):

            if index > len(nums):
                return 0

            if index == len(nums):
                if currentSum == target:
                    return 1 
                else:
                    return 0

            if (index,currentSum) in memo:
                return memo[(index,currentSum)]
            
            add      = recursion(index + 1,currentSum+nums[index])
            subtract = recursion(index + 1,currentSum-nums[index])

            ways = add + subtract

            memo[(index,currentSum)] = ways

            return add + subtract


        return recursion(0,0)
        