class Solution:
    def reverseWords(self, s: str) -> str:

        theList = []

        leftPointer = 0
        rightPointer = leftPointer
        tempString = ""

        while leftPointer <= len(s)-1:
           
            if s[rightPointer] != " ":
                if rightPointer >= len(s)-1:
                    tempString+=s[rightPointer]
                    theList.append(tempString)
                    break
                tempString+=s[rightPointer]
                rightPointer+=1
                
            if s[rightPointer] == " ":
                if len(tempString) != 0:
                    theList.append(tempString)
                    tempString = ""
                rightPointer+=1
                leftPointer = rightPointer
                continue

            leftPointer+=1

        theList = theList[::-1]
        return " ".join(list(theList))