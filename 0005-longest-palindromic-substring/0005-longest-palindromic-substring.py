class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1:
            return s
        elif len(s) == 2:
            if s[0] != s[1]:
                return s[0]
            else:
                return s

        longestString = ""

        def oddExpandTwoSideAndCheck(i):
            nonlocal longestString
            tempLongestString = ""
            leftIndex = i-1
            rightIndex = i+1
            while leftIndex >= 0 and rightIndex <= len(s)-1:
                if s[leftIndex] == s[rightIndex]:
                    leftIndex-=1 
                    rightIndex+=1
                else:
                    break
            tempLongestString = s[leftIndex+1:rightIndex]            
            if len(tempLongestString) >= len(longestString):
                longestString = tempLongestString
                

        def evenExpandTwoSideAndCheck(i):
            nonlocal longestString
            tempLongestString = ""
            leftIndex = i-1
            rightIndex = i
            while leftIndex >= 0 and rightIndex <= len(s)-1:
                if s[leftIndex] == s[rightIndex]:
                    leftIndex-=1 
                    rightIndex+=1
                else:
                    break
            tempLongestString = s[leftIndex+1:rightIndex]
            if len(tempLongestString) >= len(longestString):
                longestString = tempLongestString
                
        for i in range(len(s)):
            
            oddExpandTwoSideAndCheck(i)
            evenExpandTwoSideAndCheck(i)

        

        return longestString

        