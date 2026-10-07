class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashMap = defaultdict(list)
        for i in range(len(strs)):
            sortedWord = "".join(sorted(strs[i]))
            hashMap[sortedWord].append(strs[i])
        answer = []
        for key,valList in hashMap.items():
            answer.append(valList)
        return answer