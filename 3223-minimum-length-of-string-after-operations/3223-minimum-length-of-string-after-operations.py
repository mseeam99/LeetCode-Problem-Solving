class Solution:
    def minimumLength(self, s: str) -> int:
        hashMap = Counter(s)
        for key,val in hashMap.items():
            if val % 2 == 0:
                hashMap[key] = 2
            elif val % 2 != 0:
                hashMap[key] = 1
        totalLength = sum(hashMap.values())
        return totalLength


        