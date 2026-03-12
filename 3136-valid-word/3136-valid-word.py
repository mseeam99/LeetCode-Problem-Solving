class Solution:
    def isValid(self, word: str) -> bool:

        if len(word) < 3:
            return False
        hashMap = {}
        hashMap["a"] = 1
        hashMap["e"] = 1
        hashMap["i"] = 1
        hashMap["o"] = 1
        hashMap["u"] = 1
        vowelFound = False
        consoFound = False

        for i in range(len(word)):
            if (word[i].isalnum() == False):
                return False

            if word[i].lower() in hashMap:
                vowelFound = True
            elif word[i].lower() not in hashMap and word[i].isdigit() == False:
                consoFound = True
            


        if (consoFound == True and vowelFound == True):
            return True 
        else:
            return False


        