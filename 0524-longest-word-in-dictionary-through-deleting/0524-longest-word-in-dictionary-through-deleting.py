class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort()

        def checkLength(dictionaryWord):

            sPointer = 0
            dPointer = 0

            while sPointer < len(s) and dPointer < len(dictionaryWord):

                if s[sPointer] == dictionaryWord[dPointer]:
                    sPointer+=1
                    dPointer+=1
                else:
                    sPointer+=1
                
            if dPointer == len(dictionaryWord):
                return dictionaryWord, len(dictionaryWord)
            else:
                return "",0

        maxLength = 0
        answer = ""
        for i in range(len(dictionary)):
            ans, length = checkLength(dictionary[i])
            if length > maxLength:
                maxLength = length
                answer = ans
        return answer


        