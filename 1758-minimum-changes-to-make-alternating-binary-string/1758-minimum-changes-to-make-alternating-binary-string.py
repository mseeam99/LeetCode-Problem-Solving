class Solution:
    def minOperations(self, s: str) -> int:

        if len(s) == 2:
            if s[0] != s[1]:
                return 0
            else:
                return 1
        

        startsWithZero = "" 
        startsWithOne  = ""

        for i in range(len(s)):
            if i % 2 == 0:
                startsWithZero += "0"
            else:
                startsWithZero += "1"
        
        for i in range(len(s)):
            if i % 2 != 0:
                startsWithOne += "0"
            else:
                startsWithOne += "1"

        print(startsWithZero)
        print(startsWithOne)

        minChangeZero = 0
        minChangeOne = 0
        for i in range(len(s)):
            if s[i] != startsWithZero[i]:
                minChangeZero += 1
        
        for i in range(len(s)):
            if s[i] != startsWithOne[i]:
                minChangeOne += 1

        return min(minChangeZero,minChangeOne)



        

