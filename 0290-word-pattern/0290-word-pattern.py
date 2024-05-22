class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        myListOfS = s.split()
        hashMap = {}
        if len(pattern) != len(myListOfS):return False
        for i in range(len(pattern)):
            if pattern[i] not in hashMap:
                if myListOfS[i] not in hashMap.values():
                    hashMap[pattern[i]] = myListOfS[i]
                else:
                    return False
            elif pattern[i] in hashMap:
                tempValue = hashMap[pattern[i]]
                if tempValue != myListOfS[i]:
                    return False        
        return True