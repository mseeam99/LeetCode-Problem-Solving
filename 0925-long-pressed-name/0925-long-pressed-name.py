class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        pointerOne = 0
        pointerTwo = 0
        answer = ""
        previousChar = ""
        
        while pointerTwo <= len(typed)-1:
            if answer == name:
                for i in range(pointerTwo,len(typed)):
                    if typed[i] != answer[len(answer)-1]:
                        return False
                return True
            
            if name[pointerOne] == typed[pointerTwo]:  
                answer += name[pointerOne]
                previousChar = name[pointerOne]      
                pointerOne+=1
                pointerTwo+=1

            elif name[pointerOne] != typed[pointerTwo]:
                if typed[pointerTwo] == previousChar:
                    pointerTwo+=1
                else:
                    return False
            
        return True if name == answer else False




        