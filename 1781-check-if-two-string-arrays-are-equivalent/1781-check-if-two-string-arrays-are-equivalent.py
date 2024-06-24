class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        stringOne = ""
        stringTwo = ""

        pointerOne = 0
        pointerTwo = 0

        while pointerOne < len(word1) and pointerTwo<len(word2):
            stringOne+=word1[pointerOne]
            stringTwo+=word2[pointerTwo]
            pointerOne+=1
            pointerTwo+=1

        if pointerOne<len(word1):
            while pointerOne < len(word1):
               stringOne += word1[pointerOne]
               pointerOne+=1

        if pointerTwo<len(word2):
            while pointerTwo < len(word2):
               stringTwo += word2[pointerTwo]
               pointerTwo+=1

        return stringOne == stringTwo

        