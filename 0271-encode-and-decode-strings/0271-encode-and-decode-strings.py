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
        print(s)
        answer = []
        pointerOne = 0
        tempString = ""
        while pointerOne < len(s):
            intLenthToIncrease = ""
            for i in range(pointerOne,len(s)):
                if s[i] == "#":
                    break
                else:
                    intLenthToIncrease += s[i]
                    pointerOne+=1
            intLenthToIncrease = int(intLenthToIncrease)
            nextLoopUntil = pointerOne + intLenthToIncrease
            while pointerOne <= nextLoopUntil:
                tempString += s[pointerOne]
                pointerOne+=1
            answer.append(tempString)
            tempString = ""
        for i in range(len(answer)):
            answer[i] = answer[i][1:]
        return answer


        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))