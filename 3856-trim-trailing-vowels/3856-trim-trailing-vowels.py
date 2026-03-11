class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)-1,-1,-1):
            if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u":
                pass
            else:
                return "".join(s[:i+1])
        return ""



       
        