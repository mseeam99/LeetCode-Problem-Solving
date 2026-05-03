class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        hashMap = {}

        leftPointer = 0
        rightPointer = 0
        maxLength = 0

        while rightPointer <= len(s)-1:

        
            if s[rightPointer] not in hashMap:
                hashMap[s[rightPointer]] = 1
                rightPointer += 1
            elif s[rightPointer] in hashMap:
                hashMap[s[rightPointer]] += 1
                rightPointer += 1

            while len(hashMap) > k:
                if s[leftPointer] in hashMap:
                    hashMap[s[leftPointer]] -= 1
                    if hashMap[s[leftPointer]] == 0:
                        del hashMap[s[leftPointer]]
                leftPointer += 1

            maxLength = max(maxLength,rightPointer-leftPointer+1)

        return maxLength-1

            






