class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        tempStack = []

        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                tempStack.append(s[i])
            elif s[i] == ")":
                if len(tempStack) != 0 and tempStack[len(tempStack)-1] == "(" :
                    tempStack.pop()
                else:
                    tempStack.append(")")
            elif s[i] == "}":
                if len(tempStack) != 0 and tempStack[len(tempStack)-1] == "{":
                    tempStack.pop()
                else:
                    tempStack.append("}")
            elif s[i] == "]":
                if len(tempStack) != 0 and tempStack[len(tempStack)-1] == "[":
                    tempStack.pop()
                else:
                    tempStack.append("]")
        
        if len(tempStack) == 0:
            return True
        else:
            return False

        

        