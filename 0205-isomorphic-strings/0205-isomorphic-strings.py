class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashMap = {}
        mapped_values = set()
        for i in range(len(s)):
            if s[i] not in hashMap:
                if t[i] in mapped_values:
                    return False
                hashMap[s[i]] = t[i]
                mapped_values.add(t[i])
            elif hashMap[s[i]] != t[i]:
                return False
        return True
