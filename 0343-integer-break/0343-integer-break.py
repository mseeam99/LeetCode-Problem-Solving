from functools import cache

class Solution:
    def integerBreak(self, n: int) -> int:
        @cache
        def find_max_product(current):
            if current == 0:
                return 1

            best_product = float('-inf')

            end_range = current if current == n else current + 1
            for i in range(1, end_range):
                best_product = max(best_product, find_max_product(current - i) * i)

            return best_product

        return find_max_product(n)
