class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False
        searchingFor = totalSum // 2
        memo = {}

        def dfs(index, currentSum):
            if currentSum == searchingFor:
                return True
            if currentSum > searchingFor or index >= len(nums):
                return False
            if (index, currentSum) in memo:
                return memo[(index, currentSum)]
            result = dfs(index + 1, currentSum + nums[index]) or dfs(index + 1, currentSum)
            memo[(index, currentSum)] = result
            return result

        return dfs(0, 0)
