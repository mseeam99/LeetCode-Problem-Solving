class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        if len(word) == 1:
            return True

        allLetersCapital = False
        allLetersNOTCapital = False
        firstOneCapital = False

        if word[0].isupper():
            firstOneCapital = True

        for i in range(1,len(word)):
            if word[i].isupper():
                allLetersCapital = True
            else:
                allLetersCapital = False
                break

        for i in range(1,len(word)):
            if word[i].islower():
                allLetersNOTCapital = True
            else:
                allLetersNOTCapital = False
                break
       
        if firstOneCapital == True and allLetersCapital == True:
            return True
        
        if firstOneCapital == False and allLetersNOTCapital == True:
            return True
        
        if firstOneCapital == True and allLetersNOTCapital == True:
            return True

        return False
        

        