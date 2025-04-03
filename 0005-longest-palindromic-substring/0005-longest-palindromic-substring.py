class Solution:
    def longestPalindrome(self, s: str) -> str:

        if s == s[::-1]:
            return s

        answer = ""

        def expand(left,right):

            nonlocal answer
            
            while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
                
                left -= 1
                right += 1

            newString = ""
            
            for i in range(left+1,right):
                newString+=s[i]

            if newString == newString[::-1]:
                if len(newString) >= len(answer):
                    answer = newString
            
        for i in range(len(s)):
            expand(i,i)
            expand(i,i+1)

        return answer
            






        
        