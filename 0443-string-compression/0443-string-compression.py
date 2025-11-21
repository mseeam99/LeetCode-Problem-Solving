class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0      
        index = 0  
        while i < len(chars):
            currentChar = chars[i]
            lengthCount = 0
            while i < len(chars) and chars[i] == currentChar:
                lengthCount += 1
                i += 1
            chars[index] = currentChar
            index+=1
            if lengthCount > 1:
                numberAsString = str(lengthCount)
                for j in range(len(numberAsString)):
                    chars[index] = numberAsString[j]
                    index+=1
        return index


        