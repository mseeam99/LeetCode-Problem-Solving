class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        left, right = 0, 32
        while left <= right:
            mid = left + (right - left) // 2
            power = 4 ** mid
            if power == n:
                return True
            elif power < n:
                left = mid + 1
            else:
                right = mid - 1
        return False