class Solution:
    def findTargetSumWays(self, nums, target):
        '''
        total = sum(nums)
        if total < abs(target) or (total + target) % 2 != 0:
            return 0
        find = (total + target) // 2
        memo = {}
        def recursion(index, currentSum):
            if (index, currentSum) in memo:
                return memo[(index, currentSum)]
            if index == 0:
                if currentSum == 0 and nums[0] == 0:
                    return 2
                if currentSum == 0:
                    return 1
                if currentSum == nums[0]:
                    return 1
                return 0
            notPick = recursion(index - 1, currentSum)
            pick = 0
            if nums[index] <= currentSum:
                pick = recursion(index - 1, currentSum - nums[index])
            memo[(index, currentSum)] = pick + notPick
            return memo[(index, currentSum)]
        return recursion(len(nums) - 1, find)
        '''

        total = sum(nums)
        if total < abs(target) or (total + target) % 2 != 0:
            return 0
        find = (total + target) // 2
        n = len(nums)
        dp = [[0] * (find + 1) for _ in range(n)]
        if nums[0] == 0:
            dp[0][0] = 2
        else:
            dp[0][0] = 1

        if nums[0] != 0 and nums[0] <= find:
            dp[0][nums[0]] = 1
        for i in range(1, n):
            for currentSum in range(find + 1):
                notPick = dp[i - 1][currentSum]
                pick = 0
                if nums[i] <= currentSum:
                    pick = dp[i - 1][currentSum - nums[i]]
                dp[i][currentSum] = pick + notPick
        return dp[n - 1][find]

        

        


