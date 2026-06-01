class Solution:
    def canConstruct(self, s: str, k: int) -> bool:

        if k > len(s):
            return False

        hashMap = Counter(s)
        evenCount = 0
        oddCount = 0

        for key,val in hashMap.items():
            if val % 2 == 0:
                evenCount += 1
            else:
                oddCount += 1
        
        if oddCount <= k:
            return True

        return False



        