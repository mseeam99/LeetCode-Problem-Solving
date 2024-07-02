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



'''     
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        pointerOne = 0
        pointerTwo = pointerOne 

        tempString = ""
        hashMap = {}

        while pointerOne < len(s) and pointerTwo < len(s):
            if s[pointerTwo] not in tempString:
                tempString+=s[pointerTwo]
                pointerTwo+=1
            elif s[pointerTwo] in tempString:
                hashMap[len(tempString)] = tempString
                tempString = ""
                pointerOne+=1
                pointerTwo = pointerOne 

        hashMap[len(tempString)] = tempString
        
        if len(hashMap) != 0 :
            answer = max(hashMap)
            return answer
        else:
            return len(s)
'''     