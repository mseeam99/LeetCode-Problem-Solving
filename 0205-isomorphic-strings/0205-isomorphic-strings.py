class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashMap = {}
        myList  = []
        for i in range(len(s)):
            if s[i] not in hashMap:
                hashMap[s[i]] = t[i]
                if t[i] not in myList:
                    myList.append(t[i])
                else:
                    return False
            else:
                if hashMap[s[i]] != t[i]:
                    return False
        return True
        

