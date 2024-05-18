class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDictionary = defaultdict(list)
        for words in strs:
            sortedWord = "".join(sorted(words))
            myDictionary[sortedWord].append(words)
        return list(myDictionary.values())