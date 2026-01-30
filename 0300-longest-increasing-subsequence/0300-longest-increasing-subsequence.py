class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        # dp[index][prevIndex+1] = best LIS length from 'index' when last chosen is prevIndex
        dp = [[-1] * (n + 1) for _ in range(n)]

        def recursion(index, prevIndex):
            if index == n:
                return 0

            col = prevIndex + 1
            if dp[index][col] != -1:
                return dp[index][col]

            # not pick
            best = recursion(index + 1, prevIndex)

            # pick (only if increasing)
            if prevIndex == -1 or nums[index] > nums[prevIndex]:
                best = max(best, 1 + recursion(index + 1, index))

            dp[index][col] = best
            return best

        return recursion(0, -1)
