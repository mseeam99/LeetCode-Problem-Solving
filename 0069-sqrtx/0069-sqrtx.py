class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 1:
            return 1

        length = x
        answer = 0
        left = 0
        right = length - 1

        while left <= right:
            middle = floor((left+right) // 2)
            val = middle * middle
            if val <= x:
                answer = middle
                left += 1
            elif val < x: 
                left = middle + 1
            elif val > x: 
                right = middle - 1
            

        return answer

        