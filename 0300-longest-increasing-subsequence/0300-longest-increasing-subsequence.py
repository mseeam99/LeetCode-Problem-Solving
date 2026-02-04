class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [[-1] * (n + 1) for _ in range(n + 1)]

        def recursion(index, prevIdx):
            if index == n:
                return 0

            prevKey = prevIdx + 1  

            if dp[index][prevKey] != -1:
                return dp[index][prevKey]

            notPick = recursion(index + 1, prevIdx)

            pick = 0
            if prevIdx == -1 or nums[index] > nums[prevIdx]:
                pick = 1 + recursion(index + 1, index)

            dp[index][prevKey] = max(pick, notPick)
            return dp[index][prevKey]

        return recursion(0, -1)
