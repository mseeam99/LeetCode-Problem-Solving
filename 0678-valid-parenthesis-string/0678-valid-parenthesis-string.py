class Solution:
    def checkValidString(self, s: str) -> bool:

        open_paren = 0  
        close_paren = 0

        for char in s:
            if char == '(':
                open_paren += 1
                close_paren += 1
            elif char == ')':
                open_paren -= 1
                close_paren -= 1
            else: 
                open_paren -= 1  
                close_paren += 1 

            if close_paren < 0:
                return False

            if open_paren < 0:
                open_paren = 0 

        return open_paren == 0
