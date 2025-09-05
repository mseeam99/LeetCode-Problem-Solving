from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # If total candies are fewer than children, no one can get >= 1
        total = sum(candies)
        if total < k:
            return 0

        # Helper: can we give each child 'x' candies?
        def can_give(x: int) -> bool:
            # x must be >= 1 when called
            need = k
            for pile in candies:
                need -= pile // x
                if need <= 0:
                    return True
            return False

        # Max per-child is at most total // k (tighter than max(candies))
        left, right = 1, total // k
        ans = 0
        while left <= right:
            mid = left + (right - left) // 2
            if can_give(mid):
                ans = mid          # feasible; try larger
                left = mid + 1
            else:
                right = mid - 1    # infeasible; try smaller
        return ans
