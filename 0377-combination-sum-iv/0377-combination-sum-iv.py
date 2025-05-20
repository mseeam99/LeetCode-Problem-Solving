from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dparray = [-1] * (target + 1)

        def dp(n):
            if n > target:
                return 0
            elif n == target:
                return 1
            elif dparray[n] != -1:
                return dparray[n]

            res = 0

            for num in nums:
                res += dp(n + num)

            dparray[n] = res

            return res

        return dp(0)
