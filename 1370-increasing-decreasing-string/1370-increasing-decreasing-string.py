class Solution:
    def sortString(self, s: str) -> str:

        hashMap = {}
        for i in range(len(s)):
            if s[i] not in hashMap:
                hashMap[s[i]] = 1
            else:
                hashMap[s[i]] += 1

        answer = ""
        sortedKeys = sorted(hashMap.keys())

        while len(answer) != len(s):

            #forward pass
            for i in range(len(sortedKeys)):
                if hashMap[sortedKeys[i]] > 0:
                    answer += sortedKeys[i]
                    hashMap[sortedKeys[i]] -= 1


            # backward pass
            for i in range(len(sortedKeys)-1,-1,-1):
                if hashMap[sortedKeys[i]] > 0:
                    answer += sortedKeys[i]
                    hashMap[sortedKeys[i]] -= 1

        return answer

      