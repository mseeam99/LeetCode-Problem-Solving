class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLPalindromeLength = float("-inf")
        maxLPalindromeString = ""
        for i in range(len(s)):
            leftPointer = i
            rightPointer = i
            while leftPointer >= 0 and rightPointer <= len(s)-1 and s[leftPointer] == s[rightPointer]:
                leftPointer -= 1
                rightPointer += 1
            currentLength = rightPointer - leftPointer - 1 
            if currentLength > maxLPalindromeLength:
                maxLPalindromeLength = currentLength
                maxLPalindromeString = s[leftPointer + 1:rightPointer]

            leftPointer = i
            rightPointer = i + 1
            while leftPointer >= 0 and rightPointer <= len(s)-1 and s[leftPointer] == s[rightPointer]:
                leftPointer -= 1
                rightPointer += 1
            currentLength = rightPointer - leftPointer - 1
            if currentLength > maxLPalindromeLength:
                maxLPalindromeLength = currentLength
                maxLPalindromeString = s[leftPointer + 1:rightPointer]        
        return maxLPalindromeString
