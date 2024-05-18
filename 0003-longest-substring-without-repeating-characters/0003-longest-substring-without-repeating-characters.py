class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        hashMap = {}
        setOfChar = set()
        left = 0
        for right in range(len(s)):
            while s[right] in setOfChar:
                setOfChar.remove(s[left])
                left+=1
            setOfChar.add(s[right])
            hashMap[len(setOfChar)] = setOfChar

        answer = max(hashMap)
        return answer
            
            
            



        