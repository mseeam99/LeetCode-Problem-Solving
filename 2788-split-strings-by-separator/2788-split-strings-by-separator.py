class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        array = []
        for i in range(len(words)):
            subArrayItems = words[i].split(separator)
            for j in range(len(subArrayItems)):
                if subArrayItems[j] != "":
                    array.append(subArrayItems[j])
        return array 