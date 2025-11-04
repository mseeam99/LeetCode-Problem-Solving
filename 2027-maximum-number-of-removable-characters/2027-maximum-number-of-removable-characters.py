class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def checkIfSubsequenceAsLinear(indexMiddle):
            removableSet = set(removable[:indexMiddle+1])
            idx = 0
            newStringAFterTrimmed = ""
            for i in range(len(s)):
                if i in removableSet:
                    pass
                else:
                    newStringAFterTrimmed += s[i]
            i = 0
            j = 0
            while i < len(newStringAFterTrimmed) and j < len(p):
                if newStringAFterTrimmed[i] == p[j]:
                    i+=1
                    j+=1
                else:
                    i+=1
            return j == len(p)

        answer = 0
        left = 0
        right = len(removable)-1
        while left <= right:
            middle = left + (right-left) // 2
            if checkIfSubsequenceAsLinear(middle) == True:
                left = middle + 1
                answer = middle + 1
            else:
                right = middle - 1
        return answer



        



       
            

    