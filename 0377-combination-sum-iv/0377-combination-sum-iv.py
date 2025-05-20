from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dpa = [-1] * (target + 1)

        def dp(n):
            if n > target:
                return 0
            elif n == target:
                return 1
            elif dpa[n] != -1:
                return dpa[n]
            res = 0
            for num in nums:
                res += dp(n + num)
            dpa[n] = res
            return res

        return dp(0)
