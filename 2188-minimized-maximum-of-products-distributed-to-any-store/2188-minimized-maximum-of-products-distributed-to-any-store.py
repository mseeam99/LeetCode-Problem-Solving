import math
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        def storeNeeded(x):
            nonlocal quantities, n
            storeNeeded = 0
            for i in range(len(quantities)):
                storeNeeded += math.ceil(quantities[i] / x)
            if storeNeeded <= n:
                return True
            else:
                return False
                
        left = 1
        right = max(quantities)
        while left <= right:
            middle = left + (right-left) // 2
            if storeNeeded(middle) == True:
                right = middle - 1
            else:
                left = middle + 1
        return left        