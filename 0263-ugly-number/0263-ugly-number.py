class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        allowed = [2,3,5]
        for val in allowed:
            while n % val == 0:
                n = n // val
            if n == 1:
                return True 
        return False


        