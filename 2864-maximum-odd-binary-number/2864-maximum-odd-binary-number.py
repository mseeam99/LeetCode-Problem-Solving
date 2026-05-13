class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:

        oneCount = 0
        zeroCount = 0

        for i in range(len(s)):
            if s[i] == "1":
                oneCount += 1
            else:
                zeroCount += 1

        answer = ""

        for i in range(oneCount-1):
            answer += "1"
        for i in range(zeroCount):
            answer += "0"
        answer += "1"


        





        return answer





        