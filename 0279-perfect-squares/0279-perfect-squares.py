from math import isqrt
from functools import lru_cache

class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i * i for i in range(1, isqrt(n) + 1)]

        @lru_cache(maxsize=None)
        def min_squares(remaining):
            if remaining == 0:
                return 0
            if remaining < 0:
                return float('inf')

            min_count = float('inf')
            for square in squares:
                if square <= remaining:
                    count = 1 + min_squares(remaining - square)
                    min_count = min(min_count, count)
            return min_count

        return min_squares(n)
