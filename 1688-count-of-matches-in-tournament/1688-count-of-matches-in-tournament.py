from math import floor 
class Solution:
    def numberOfMatches(self, n: int) -> int:
        proceed = 0
        while n != 0:
            if n%2 != 0 :
                proceed += (ceil(n - 1) / 2)+1
                n = floor(n - 1) / 2
            elif n%2 == 0:
                proceed += n // 2
                n = n // 2
        return int(proceed-1)
                
        