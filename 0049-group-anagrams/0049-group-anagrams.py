class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashMap = defaultdict(list)
        for i in range(len(strs)):
            sortedWord = "".join(sorted(strs[i]))
            hashMap[sortedWord].append(i)
        answer = []
        for key,valList in hashMap.items():
            smallArray = []
            for i in range(len(valList)):
                smallArray.append(strs[valList[i]])
            answer.append(smallArray)
        return answer
                


