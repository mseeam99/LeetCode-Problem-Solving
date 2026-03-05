class Solution:
    def maxDifference(self, s: str) -> int:
        hashMap = Counter(s)
        maxOdd = 0
        minEven = float('inf')
        for key,val in hashMap.items():
            if val % 2 == 1:
                maxOdd = max(maxOdd,val)
            elif val % 2 == 0:
                minEven = min(minEven,val)
        return maxOdd - minEven
