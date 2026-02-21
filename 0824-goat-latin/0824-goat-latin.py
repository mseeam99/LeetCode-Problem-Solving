class Solution:
    def toGoatLatin(self, sentence: str) -> str:

        array = sentence.split(" ")

        for i in range(len(array)):
            changedString = ""
            currentWord = array[i]
            if currentWord[0].lower() == "a" or currentWord[0].lower() == "e" or currentWord[0].lower() == "i" or currentWord[0].lower() == "o" or currentWord[0].lower() == "u":
                modifiedWord = currentWord+"ma"
                aAdded = "a" * (i+1)
                modifiedWord += aAdded
                if i != len(array)-1:
                    modifiedWord+=" "
                array[i] = modifiedWord
            else:
                for j in range(1,len(currentWord)):
                    changedString += currentWord[j]
                changedString += currentWord[0]
                currentWord = changedString
                modifiedWord = currentWord+"ma"
                aAdded = "a" * (i+1)
                modifiedWord += aAdded
                if i != len(array)-1:
                    modifiedWord+=" "
                array[i] = modifiedWord
            
        
        return "".join(array)

                







        