class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2 != 0:
            return False
        left = []
        star = []
        for i in range(len(s)):
            if locked[i] == "0":
                star.append(i)
            elif s[i] == "(":
                left.append(i)
            elif s[i] == ")":
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while left and star and (left[-1] < star[-1]):    
            left.pop()
            star.pop()
        if left:
            return False
        return True