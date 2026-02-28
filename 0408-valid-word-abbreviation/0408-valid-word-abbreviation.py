class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        wordPointer = 0
        abbrPointer = 0

        while wordPointer <= len(word)-1 and abbrPointer <= len(abbr)-1:
            if abbr[abbrPointer].isdigit() == True:
                if abbr[abbrPointer] == "0":
                    return False
                trackIndexApproach = ""
                while abbrPointer <= len(abbr)-1 and abbr[abbrPointer].isdigit() == True:
                    trackIndexApproach += abbr[abbrPointer]
                    abbrPointer += 1
                trackIndexApproach = int(trackIndexApproach)
                wordPointer += trackIndexApproach
                if wordPointer > len(word):
                    return False
            else:
                if abbr[abbrPointer] != word[wordPointer]:
                    return False
                wordPointer += 1
                abbrPointer += 1
                
        if wordPointer == len(word) and abbrPointer == len(abbr):
            return True
        else:
            return False
                    





                
            






                
            



                    

                    
                    