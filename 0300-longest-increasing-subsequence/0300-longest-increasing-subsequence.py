from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n  # memo[i] stores LIS starting at index i

        def dfs(i: int) -> int:
            if memo[i] != -1:
                return memo[i]

            max_len = 1  # At least the element itself
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    max_len = max(max_len, 1 + dfs(j))

            memo[i] = max_len
            return memo[i]

        return max(dfs(i) for i in range(n))
