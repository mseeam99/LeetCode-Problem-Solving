import math

class Solution:
    def numSquares(self, n: int) -> int:
        if n == 1:
            return 1

        # Precompute squares in descending order (so we try big squares first for faster pruning)
        max_root = math.isqrt(n)
        numbers = [i*i for i in range(max_root, 0, -1)]
        print(numbers)

        least = float('inf')
        memo = {}  # memo[rem] = best (smallest) coinCount we've used so far to reach rem

        def dfs(rem: int, coinCount: int):
            nonlocal least

            # 1) If we've already used at least as many coins as the best solution, stop
            if coinCount >= least:
                return

            # 2) If we've been in this state with an equal or better coinCount, stop
            if rem in memo and coinCount >= memo[rem]:
                return
            # record that we're exploring rem with coinCount
            memo[rem] = coinCount

            # 3) If we hit zero, update global best
            if rem == 0:
                least = coinCount
                return

            # 4) Recurse, but skip any square > rem
            for sq in numbers:
                if sq > rem:
                    continue
                dfs(rem - sq, coinCount + 1)

        dfs(n, 0)
        return least
