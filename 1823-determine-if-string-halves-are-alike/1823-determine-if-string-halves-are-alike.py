class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        halfLength = len(s)//2
        firstHalf = s[:halfLength]
        secondHalf = s[halfLength:]
        vowel = "aeiouAEIOU"
        firstHalfCount  = 0
        secondHalfCount = 0
        for i in range(len(firstHalf)):
            if firstHalf[i] in vowel:
                firstHalfCount+=1
            if secondHalf[i] in vowel:
                secondHalfCount+=1        
        return firstHalfCount == secondHalfCount
        