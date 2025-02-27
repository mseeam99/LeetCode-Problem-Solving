class Solution:
    def isHappy(self, n: int) -> bool:
        
        theString = str(n)

        for i in range(100):
            val = 0
            for i in range(len(theString)):
                val += ((int(theString[i]))**2)
            if val == 1:
                return True
            print(val)
            theString = str(val)

        return False



        