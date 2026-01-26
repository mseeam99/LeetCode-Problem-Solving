class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        hashMap = {}

        for i in range(len(magazine)):
            if magazine[i] not in hashMap:
                hashMap[magazine[i]] = 1
            else:
                hashMap[magazine[i]] += 1

        for i in range(len(ransomNote)):
            if ransomNote[i] in hashMap:
                if hashMap[ransomNote[i]] <= 0:
                    return False
                else:
                    hashMap[ransomNote[i]] -= 1
            else:
                return False

        for key,val in hashMap.items():
            if val < 0:
                return False
        
        return True