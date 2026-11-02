class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        s = ""
        for i in range(len(strs)):
            string = strs[i]
            length = len(string)
            s+=str(length)
            s+="#"
            s+=string
        return s
        
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        answer = []
        pointerOne = 0
        while pointerOne <= len(s)-1:
            currentPointer = pointerOne
            numberString = ""
            numberInt = 0
            while s[currentPointer] != "#":
                numberString += s[currentPointer]
                currentPointer += 1
            numberInt = int(numberString)
            currentPointer += 1
            extractedString = s[currentPointer:currentPointer+numberInt]
            pointerOne = currentPointer+numberInt
            answer.append(extractedString)
            numberString = ""
            numberInt = 0
        return answer
            









        

        
        
        
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))