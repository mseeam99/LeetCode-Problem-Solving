class Solution:
    def numberCount(self, a: int, b: int) -> int:

        def calculateIfADigitIsUnique(val):
            s = str(abs(val)) 
            if len(set(s)) == len(s):
                return True
            return False
            
        count = 0
        for i in range(a,b+1):
            ans = calculateIfADigitIsUnique(i)
            if ans == True:
                count+=1
        return count




        