class Solution:
    def isPalindrome(self, s: str) -> bool:

        def palindromeEven(s):
            leftPointer = 0
            rightPointer = len(s)-1
            isPalindrome = True
            while leftPointer <= rightPointer:
                if leftPointer == rightPointer:
                    return True
                if s[leftPointer].isalnum()==False and s[rightPointer].isalnum()==False:
                    leftPointer += 1
                    rightPointer -= 1 
                    continue
                if s[leftPointer].isalnum()==False:
                    leftPointer += 1
                    continue
                if s[rightPointer].isalnum()==False:
                    rightPointer -= 1
                    continue
                if s[leftPointer].lower() == s[rightPointer].lower():
                    leftPointer += 1
                    rightPointer -= 1
                else:
                    isPalindrome = False
                    break
            return isPalindrome

        return palindromeEven(s)
        