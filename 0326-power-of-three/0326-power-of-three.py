class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        answer = False
        left = 0
        right = 32
        while left <= right:
            middle = left + (right-left) // 2
            currentPowerValue = (3**middle)
            if currentPowerValue == n:
                answer = True
                break
            elif currentPowerValue < n:
                left = middle + 1
            elif currentPowerValue > n:
                right = middle - 1
        return answer


        