class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vCount = 0
        cCount = 0
        for i in range(len(s)):
            if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u":
                vCount+=1
            elif "a" <= s[i] <= "z":
                cCount+=1
            else:
                continue
        if cCount != 0:
            return floor(vCount/cCount)
        else:
            return 0



        