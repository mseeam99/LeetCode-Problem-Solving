class Solution:
    def checkValidString(self, s: str) -> bool:

        leftArray = []
        starArray = []


        for i in range(len(s)):

            if s[i] == "(":
                leftArray.append(i)
            elif s[i] == "*":
                starArray.append(i)
            else:
                if not leftArray and not starArray:
                    return False
                elif leftArray:
                    leftArray.pop()
                elif starArray:
                    starArray.pop()

        while leftArray and starArray:
            if leftArray.pop() > starArray.pop():
                return False
        
        
        return not leftArray
                    


      