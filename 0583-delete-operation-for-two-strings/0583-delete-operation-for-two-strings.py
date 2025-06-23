fmax = lambda x,y: x if x > y else y
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        answer = 0
        def recursion(indexOne,indexTwo):
            nonlocal answer
            if (indexOne,indexTwo) in memo:
                return memo[(indexOne,indexTwo)]
            if indexOne >= len(word1) or indexTwo >= len(word2):
                return 0
            elif word1[indexOne] == word2[indexTwo]:
                return (1 + recursion(indexOne+1,indexTwo+1))
            else:
                x = recursion(indexOne+1,indexTwo)
                y = recursion(indexOne,indexTwo+1)
                memo[(indexOne,indexTwo)] = max(x,y)
                return max(x,y)
        answer = recursion(0,0)
        return (len(word1) + len(word2) - answer*2)

        