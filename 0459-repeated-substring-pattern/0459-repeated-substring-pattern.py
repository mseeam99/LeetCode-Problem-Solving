class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        currentString = ""
        for j in range(len(s)):
            currentString += s[j]
            if len(s) % len(currentString) != 0:
                continue
            multiplyBy = len(s) // len(currentString)
            if multiplyBy >= 2 and (currentString * multiplyBy == s):
                return True
        return False