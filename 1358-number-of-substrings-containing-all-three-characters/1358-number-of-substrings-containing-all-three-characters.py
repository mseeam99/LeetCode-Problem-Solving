class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        hashMap = {}
        answer = 0

        for i in range(len(s)):
            
            hashMap[s[i]] = i

            if len(hashMap) == 3:
                minIndex = min(hashMap.values())
                answer += minIndex+1

        return answer 



            




        