class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        hashMap = {}
        leftPointer = 0
        rightPointer = 0
        count = 0
        while rightPointer <= len(s)-1:
            if s[rightPointer] not in hashMap:
                hashMap[s[rightPointer]] = 1
            elif s[rightPointer] in hashMap:
                hashMap[s[rightPointer]] += 1
            while rightPointer - leftPointer + 1 > k:
                hashMap[s[leftPointer]] -= 1
                if hashMap[s[leftPointer]] == 0:
                    del hashMap[s[leftPointer]]
                leftPointer += 1
            if rightPointer - leftPointer + 1 == k and len(hashMap) == k:
                count += 1
            rightPointer += 1
        return count