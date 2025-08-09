class Solution:
    def checkRecord(self, s: str) -> bool:
        hashMap = {}
        for i in range(len(s)):
            if s[i] not in hashMap:
                hashMap[s[i]] = 1
            else:
                hashMap[s[i]] += 1
        Acount = 0
        Lcount = 0
        if "A" in hashMap:
            Acount = hashMap["A"]
        if "L" in hashMap:
            Lcount = hashMap["L"]
        return True if (Acount < 2 and "LLL" not in s) else False 