class Solution:
    def validPalindrome(self, s: str) -> bool:
        
       
        
        def palindrome(s):
            leftPointer = 0
            rightPointer = len(s)-1
            while leftPointer <= rightPointer:
                if leftPointer == rightPointer:
                    break
                if s[leftPointer].isalnum()==False and s[rightPointer].isalnum()==False:
                    leftPointer += 1
                    rightPointer -= 1 
                    continue
                if s[leftPointer].isalnum()==False:
                    eftPointer += 1
                    continue
                if s[rightPointer].isalnum()==False:
                    rightPointer -= 1
                    continue
                if s[leftPointer].lower() == s[rightPointer].lower():
                    leftPointer += 1
                    rightPointer -= 1
                else:
                    return False
            return True
        

        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return palindrome(s[l+1:r+1]) or palindrome(s[l:r])
            l += 1
            r -= 1

        return True