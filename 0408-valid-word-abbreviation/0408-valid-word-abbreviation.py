class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        wordPointer = 0
        abbrPointer = 0

        while wordPointer <= len(word)-1 and abbrPointer <= len(abbr)-1:
                    
            if abbrPointer <= len(abbr)-1 and abbr[abbrPointer].isdigit() == True:
                if abbr[abbrPointer] == "0":
                    return False
                trackIndexApproach = 0
                while abbrPointer <= len(abbr)-1 and abbr[abbrPointer].isdigit() == True:
                    trackIndexApproach = trackIndexApproach * 10 + (ord(abbr[abbrPointer]) - ord('0'))
                    abbrPointer += 1
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
                    





                
            






                
            



                    

                    
                    