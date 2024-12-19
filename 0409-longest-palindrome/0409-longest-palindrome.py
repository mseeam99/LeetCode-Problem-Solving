class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        mySet = set()
        for i in range(len(s)):
            if s[i] in mySet:
                mySet.remove(s[i])
                count += 2
            else:    
                mySet.add(s[i])
        return count+1 if mySet else count        