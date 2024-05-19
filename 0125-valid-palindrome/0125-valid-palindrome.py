class Solution:
    def isPalindrome(self, s: str) -> bool:
        leftPointer = 0
        rightPointer = len(s) - 1
        while leftPointer < rightPointer:
            if s[leftPointer].isalnum() == False:
                leftPointer+=1
            elif s[rightPointer].isalnum() == False:
                rightPointer-=1
            elif s[leftPointer].lower() == s[rightPointer].lower():
                leftPointer+=1
                rightPointer-=1
            else:
                return False
        return True