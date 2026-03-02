class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:


        stringArray = s1 + " " + s2
        stringArray = stringArray.split(" ")
        hashMap = {}

        for i in range(len(stringArray)):
            if stringArray[i] not in hashMap:
                hashMap[stringArray[i]] = 1
            else:
                hashMap[stringArray[i]] += 1
        
        answer = []
        for key, val in hashMap.items():
            if val == 1:
                answer.append(key)

        return answer
                

        