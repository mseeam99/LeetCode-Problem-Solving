class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxNumberOfWords = float("-inf")
        for i in range(len(sentences)):
            maxNumberOfWords = max(maxNumberOfWords,len(sentences[i].split(" ")))
        return maxNumberOfWords
        