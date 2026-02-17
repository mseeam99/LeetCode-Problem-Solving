class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ans = 0
        array = text.split(" ")
        if brokenLetters == "":
            return len(array)
        if text == "":
            return 0
        for i in range(len(array)):
            word = array[i]
            for j in range(len(brokenLetters)):
                if brokenLetters[j] not in word:
                    pass
                else:
                    break
                if j == len(brokenLetters)-1:
                    ans+=1
             
        return ans



        

        