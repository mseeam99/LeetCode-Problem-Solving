class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashMap = {}
        for i in range(len(s)):
            if s[i] not in hashMap:
                hashMap[s[i]] = 1
            else:
                hashMap[s[i]]+=1

        extraChar = ""
        for i in range(len(t)):
            if t[i] in hashMap:
                hashMap[t[i]]-=1
                if hashMap[t[i]] < 0:
                    extraChar = t[i]
            elif t[i] not in hashMap:
                extraChar = t[i]
        
        return extraChar


                
        
            

        