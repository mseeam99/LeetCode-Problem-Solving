class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:

        answer = 0

        for i in range(len(s)):
            zeroCount = 0
            oneCount = 0
            for j in range(i,len(s)):

                
                currentDigit = s[j]
                if currentDigit == "1":
                    oneCount += 1
                elif currentDigit == "0":
                    zeroCount += 1

                if zeroCount > k and oneCount > k:
                    break
                    
                answer += 1 

        return answer


        