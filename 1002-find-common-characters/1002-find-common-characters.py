class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        firstHashMap = Counter(words[0])

        for i in range(1,len(words)):
            currentHashMap = Counter(words[i])
            for key,val in firstHashMap.items():
                if key in currentHashMap:
                    firstHashMap[key] = min(firstHashMap[key],currentHashMap[key])
                else:
                    firstHashMap[key] = 0


        answer = []
        for key,val in firstHashMap.items():
            for _ in range(val):
                answer.append(key)

        return answer


        

        

