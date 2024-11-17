class Solution:
    def reverseVowels(self, s: str) -> str:
        
        givenValue = list(s)
        leftPointer  = 0
        rightPointer = len(givenValue)-1
        vowels = "aeiouAEIOU"

        while leftPointer < rightPointer:

            while givenValue[leftPointer] not in vowels and leftPointer < rightPointer:
                leftPointer+=1
                
            while givenValue[rightPointer] not in vowels and leftPointer < rightPointer:
                rightPointer-=1
            
            if givenValue[leftPointer] in vowels and givenValue[rightPointer] in vowels:
                givenValue[leftPointer],givenValue[rightPointer] = givenValue[rightPointer],givenValue[leftPointer]
                leftPointer+=1
                rightPointer-=1

        return "".join(givenValue)

        