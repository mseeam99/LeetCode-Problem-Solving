class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        memo = {}

        def recursion(indexOne,indexTwo):
            nonlocal text1, text2, memo

            if (indexOne,indexTwo) in memo:
                return memo[(indexOne,indexTwo)]

            if indexOne >= len(text1) or indexTwo >= len(text2):
                return 0
            elif text1[indexOne] == text2[indexTwo]:
                return (1 + recursion(indexOne+1,indexTwo+1))
            else:
                leftTree  = recursion(indexOne+1,indexTwo)
                rightTree = recursion(indexOne,indexTwo+1)
                memo[indexOne,indexTwo] = max(leftTree,rightTree)
                return max(leftTree,rightTree)
            return 

        return recursion(0,0)
        