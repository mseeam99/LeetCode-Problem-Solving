class Solution:
    def longestPalindrome(self, s: str) -> str:
        currentLongest = [0,1]
        for i in range(1,len(s)):
            odd  = self.expandAroundCenter(s,i-1,i+1)
            even = self.expandAroundCenter(s,i-1,i)
            if (odd[1] - odd[0]) > (even[1] - even[0]):
                longest = odd
            else:
                longest = even        
            if (longest[1] - longest[0]) > (currentLongest[1] - currentLongest[0]):
                currentLongest = longest
        return s[currentLongest[0]:currentLongest[1]]

    def expandAroundCenter(self, string, left, right):
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1
        return [left + 1, right]

