class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        pointerOne = 0
        pointerTwo = 0
        newString = ""

        while pointerOne < len(word1) and pointerTwo < len(word2) :
            newString+=word1[pointerOne]
            newString+=word2[pointerTwo]
            pointerOne+=1
            pointerTwo+=1

        if pointerOne < len(word1):
            while pointerOne < len(word1):
                newString+=word1[pointerOne]
                pointerOne+=1
        elif pointerTwo < len(word2):
            while pointerTwo < len(word2):
                newString+=word2[pointerTwo]
                pointerTwo+=1
        
        return newString





        



        