class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "]":
                tempString = ""
                while stack:
                    c = stack.pop()
                    if 'a' <= c <= 'z':
                        tempString += c
                    elif c == "[":
                        break
                numberStr = ""
                if stack:
                    while stack:
                        c = stack.pop()
                        if not ('0' <= c <= '9'):  
                            stack.append(c)  
                            break
                        numberStr += c
                numberStr = numberStr[::-1]
                tempString = tempString[::-1]
                tempLongString = tempString * int(numberStr)
                for c in tempLongString:
                    stack.append(c)
            else:
                stack.append(char)
        
        temp = ""
        while stack:
            temp += stack.pop()
        temp = temp[::-1]
        stack.append(temp)
        stack = stack[::-1]
        return "".join(stack)

   



        