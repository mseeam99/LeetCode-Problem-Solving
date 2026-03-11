class Solution:
    def maxFreqSum(self, s: str) -> int:

        vowelHashMap = {}
        consoHashMap = {}

        for i in range(len(s)):

            if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u":
                if s[i] not in vowelHashMap:
                    vowelHashMap[s[i]] = 1
                else:
                    vowelHashMap[s[i]] += 1
            else:
                if s[i] not in consoHashMap:
                    consoHashMap[s[i]] = 1
                else:
                    consoHashMap[s[i]] += 1

        vowelMax = 0
        if len(vowelHashMap) >= 1:
            vowelMax = max(vowelHashMap.values())
        consonentMax = 0
        if len(consoHashMap) >= 1:
            consonentMax = max(consoHashMap.values())
    

        return vowelMax + consonentMax



        