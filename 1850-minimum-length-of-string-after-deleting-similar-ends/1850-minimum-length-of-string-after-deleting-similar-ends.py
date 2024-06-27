class Solution:
    def minimumLength(self, s: str) -> int:

        if len(s) == 1:
            return len(s)
        if len(s) == 2 and s[0] != s[1]:
            return len(s)
        if len(s) == 3:
            if s[0] == s[2] and s[0] != s[1]:
                return 1
        if s == s[::-1]:
            return 0

        leftPointer     = 0
        rightPointer    = len(s) - 1

        while leftPointer < rightPointer:
            tempLeftChar  = s[leftPointer]
            tempRightChar = s[rightPointer]
            if s[leftPointer] == s[rightPointer]:
                while s[leftPointer] == tempLeftChar:
                    leftPointer+=1
                while s[rightPointer] == tempRightChar:
                    rightPointer-=1
            else:
                return len(s[leftPointer:rightPointer+1])
        return len(s[leftPointer:rightPointer+1])





        