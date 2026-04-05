class Solution:
    def countSubstrings(self, s: str) -> int:
    
        answerCount = 0
        memo = {}

        def recursion(index,currentString):

            nonlocal answerCount, memo

            if (index,currentString) in memo:
                return memo[(index,currentString)]

            if index >= len(s):
                return 0 
            
            currentString = currentString+s[index]

            if currentString == currentString[::-1]:
              #  print(currentString)
                answerCount += 1
                

            #pick
            recursion(index+1,currentString)


           
            


        for i in range(len(s)):
            recursion(i,"")
        return answerCount
            
