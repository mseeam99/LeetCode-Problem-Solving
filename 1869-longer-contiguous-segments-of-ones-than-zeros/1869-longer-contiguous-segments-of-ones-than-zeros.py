class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        
        longestOneLength = 0
        longestZeroLength = 0

        for i in range(len(s)):
            currentOneLength = 0
            for j in range(i,len(s)):
                if s[j] == "1":
                    currentOneLength+=1
                else:
                    break
            longestOneLength = max(longestOneLength,currentOneLength)

        for i in range(len(s)):
            currentZeroLength = 0
            for j in range(i,len(s)):
                if s[j] == "0":
                    currentZeroLength+=1
                else:
                    break
            longestZeroLength = max(longestZeroLength,currentZeroLength)

        if longestOneLength > longestZeroLength:
            return True
        else:
            return False





        