class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        bigPointer = 0
        smallPointer = 0
        while bigPointer < len(t) and smallPointer<len(s):
            if smallPointer == len(s): break
            if t[bigPointer] == s[smallPointer]:
                bigPointer+=1
                smallPointer+=1
            else:
                bigPointer+=1
        if smallPointer == len(s): return True
        else: return False