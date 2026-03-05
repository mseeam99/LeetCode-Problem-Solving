class Solution:
    def makeFancyString(self, s: str) -> str:
        pointerOne = 0
        pointerTwo = 0
        sameCharCount = 0
        returnString = ""
        while pointerOne <= len(s)-1 and pointerTwo <= len(s)-1: 

            while pointerTwo <= len(s)-1 and s[pointerTwo] == s[pointerOne] and sameCharCount < 2:
                returnString += s[pointerTwo]
                sameCharCount += 1
                pointerTwo += 1
            sameCharCount = 0

            while pointerTwo <= len(s)-1 and s[pointerTwo] == s[pointerOne]:
                pointerTwo += 1
            
            pointerOne = pointerTwo






        return returnString
        