class Solution:
    def greatestLetter(self, s: str) -> str:
        counter = Counter(s)
        lastGreaterChar = ""
        for i in range(len(s)):
            if (s[i] >= lastGreaterChar) and (s[i].lower() in counter) and (s[i].upper() in counter):
                lastGreaterChar = s[i]
        return lastGreaterChar.upper()

