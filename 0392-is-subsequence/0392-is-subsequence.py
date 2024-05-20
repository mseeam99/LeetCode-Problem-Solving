class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointerSmall = 0
        pointerBig   = 0
        while pointerSmall<len(s) and pointerBig<len(t):
            if s[pointerSmall] == t[pointerBig]:
                pointerSmall+=1
                pointerBig+=1
            else:
                pointerBig+=1
        if pointerSmall == len(s):
            return True
        else:
            return False


        