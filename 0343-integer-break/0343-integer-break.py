from functools import cache

class Solution:
    def integerBreak(self, n: int) -> int:
        @cache
        def dp(cur):
            # base case
            if cur == 0:
                return 1

            max_product = -float('inf')
            for i in range(1, cur + 1 if cur != n else cur):
                max_product = max(max_product, dp(cur - i) * i)
            return max_product

        return dp(n)
