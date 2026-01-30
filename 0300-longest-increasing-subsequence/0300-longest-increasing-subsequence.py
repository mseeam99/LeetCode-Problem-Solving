class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 0:
            return 0

        dp = [[-1] * (n + 1) for _ in range(n)]

        def recursion(i, prev):
            if i == n:
                return 0

            col = prev + 1
            if dp[i][col] != -1:
                return dp[i][col]

            notPick = recursion(i + 1, prev)

            pick = 0
            if prev == -1 or nums[i] > nums[prev]:
                pick = 1 + recursion(i + 1, i)

            dp[i][col] = max(pick, notPick)
            return dp[i][col]

        return recursion(0, -1)
