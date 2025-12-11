class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        left = 0
        right = 31
        answer = False
        while left <= right:
            middle = left + (right-left) // 2
            if (2**middle) == n:
                answer = True
                break
            elif (2**middle) < n:
                left = middle + 1
            elif (2**middle) > n:
                right = middle - 1
        return answer
