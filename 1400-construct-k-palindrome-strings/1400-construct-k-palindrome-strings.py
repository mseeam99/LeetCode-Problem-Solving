class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        hashMap = Counter(s)

        even = 0
        odd = 0

        for key,val in hashMap.items():
            if val % 2 != 0:
                odd += 1
        
        if odd <= k:
            return True
        return False
