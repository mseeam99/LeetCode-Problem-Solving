class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        hashMap = {}

        leftPointer = 0
        rightPointer = 0

        maxFrequency = 0
        maxLength = 0
        longest_substring_length = 0

        while rightPointer <= len(s)-1:

            if s[rightPointer] not in hashMap:
                hashMap[s[rightPointer]] = 1
                maxFrequency = max(maxFrequency,max(hashMap.values()))
            else:
                hashMap[s[rightPointer]] += 1
                maxFrequency = max(maxFrequency,max(hashMap.values()))

            while (rightPointer + 1 - leftPointer - maxFrequency > k):
                
                hashMap[s[leftPointer]] -= 1
                leftPointer += 1

            maxLength = rightPointer + 1 - leftPointer
            rightPointer += 1

        return maxLength



