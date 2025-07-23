class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hashMap = {}
        for i in range(len(s)):
            if s[i] not in hashMap:
                hashMap[s[i]] = 1
            else:
                hashMap[s[i]]+=1
        
        print(hashMap)

        oneValue = hashMap[s[0]]
        for key,val in hashMap.items():
            if val != oneValue:
                return False

        return True
        
        