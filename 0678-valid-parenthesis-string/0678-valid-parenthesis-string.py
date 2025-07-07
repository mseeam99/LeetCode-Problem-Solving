class Solution:
    def checkValidString(self, s: str) -> bool:

        leftParen = []
        star = []

        for i in range(len(s)):
            char = s[i]
            if char == "(":
                leftParen.append(i)
            elif char == "*":
                star.append(i)
            elif char == ")":
                if leftParen:
                    leftParen.pop()
                elif star:
                    star.pop()
                else:
                    return False

        while star and leftParen:
            if leftParen[-1] < star[-1]:
                star.pop()
                leftParen.pop()
            else:
                return False
                
        if len(leftParen) == 0:
            return True
        else:
            return False
    
