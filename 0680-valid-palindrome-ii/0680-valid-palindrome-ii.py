class Solution:
    def validPalindrome(self, s: str) -> bool:
        leftPointer = 0
        rightPointer = len(s) - 1
        while leftPointer < rightPointer:
            if s[leftPointer] == s[rightPointer]:
                leftPointer+=1
                rightPointer-=1
            else:
                first  = self.isPalindrome(leftPointer+1,rightPointer,s)
                second = self.isPalindrome(leftPointer,rightPointer-1,s)
                return first or second
        return True



    def isPalindrome(self,left,right,s):
            return s[left:right+1] == s[left:right+1][::-1]
                    



        

        