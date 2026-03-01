class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        leftPointer = 0
        rightPointer = len(s)-1
        s = list(s)

        while leftPointer < rightPointer:
            if s[leftPointer].isalpha() == True and s[rightPointer].isalpha() == True:
                s[leftPointer], s[rightPointer] = s[rightPointer], s[leftPointer]
                leftPointer += 1
                rightPointer -= 1
            elif s[leftPointer].isalpha() == False:
                leftPointer += 1
            elif s[rightPointer].isalpha() == False:
                rightPointer -= 1


        return "".join(s)

            

        