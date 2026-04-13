class Solution:
    def findTargetSumWays(self, nums, target):

        memo = {}

        def recursion(index, currentSum):

            if (index, currentSum) in memo:
                return memo[(index, currentSum)]

            if index == 0:
                ways = 0

                if currentSum + nums[0] == 0:
                    ways += 1

                if currentSum - nums[0] == 0:
                    ways += 1

                return ways

            add = recursion(index - 1, currentSum + nums[index])
            subtract = recursion(index - 1, currentSum - nums[index])

            memo[(index, currentSum)] = add + subtract

            return add + subtract

        return recursion(len(nums) - 1, target)