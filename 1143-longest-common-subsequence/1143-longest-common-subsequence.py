class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        memo = {}

        def recursion(indexOfText1, indexOfText2):

            nonlocal memo

            if (indexOfText1 >= len(text1)) or (indexOfText2 >= len(text2)):
                return 0

            if (indexOfText1, indexOfText2) in memo:
                return memo[(indexOfText1, indexOfText2)]
            
            if (text1[indexOfText1] == text2[indexOfText2]):
                val = (1 + recursion(indexOfText1+1, indexOfText2+1))
                memo[(indexOfText1, indexOfText2)] = val
                return val
            else:
                x = recursion(indexOfText1, indexOfText2+1)
                y = recursion(indexOfText1+1, indexOfText2)
                val = max(x,y)
                memo[(indexOfText1, indexOfText2)] = val
                return val

        return recursion(0,0)
            


            
            


            



        