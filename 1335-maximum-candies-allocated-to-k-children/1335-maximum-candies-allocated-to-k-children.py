from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total = sum(candies)
        if total < k:
            return 0

        def can_give(x: int) -> bool:
            need = k
            for pile in candies:
                need -= pile // x
                if need <= 0:
                    return True
            return False

        left, right = 1, total // k
        ans = 0
        while left <= right:
            mid = left + (right - left) // 2
            if can_give(mid):
                ans = mid          
                left = mid + 1
            else:
                right = mid - 1   
        return ans