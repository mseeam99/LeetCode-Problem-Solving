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

            
            is_valid = (rightPointer + 1 - leftPointer - maxFrequency <= k)
            if not is_valid:
                hashMap[s[leftPointer]] -= 1
                leftPointer += 1

            # the window is valid at this point, store length
            # size of the window never decreases
            
            longest_substring_length = rightPointer + 1 - leftPointer
            rightPointer += 1

        return longest_substring_length



