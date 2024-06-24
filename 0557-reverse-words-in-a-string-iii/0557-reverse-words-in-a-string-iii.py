class Solution:
    def reverseWords(self, s: str) -> str:
        answer = ""
        tempWord = ""
        count = 0
        for i in range(len(s)):
            count = i
            if s[i] == " ":
                tempWord = tempWord[::-1]
                tempWord += " "
                answer+=tempWord
                tempWord = ""
            else:
                tempWord+=s[i]
        
        for i in range(len(s),count):
            tempWord+=s[i]
        
        answer += tempWord[::-1]
        
        return answer
        

        
        