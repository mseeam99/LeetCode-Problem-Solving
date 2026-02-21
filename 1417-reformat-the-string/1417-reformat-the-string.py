class Solution:
    def reformat(self, s: str) -> str:

        if len(s) == 1:
            return s
        
        charArray = []
        numArray = []

        for i in range(len(s)):
            if s[i].isnumeric():
                numArray.append(s[i])
            else:
                charArray.append(s[i])

        if len(charArray) == 0 or len(numArray) == 0 or (len(charArray) - len(numArray)) > 1:
            return ""
        
        answer = ""
        i = 0

        if len(charArray) >= len(numArray):
            for i in range(min(len(charArray),len(numArray))):
                answer += charArray[i]
                answer += numArray[i]
        else:
            for i in range(min(len(charArray),len(numArray))):
                answer += numArray[i]
                answer += charArray[i]
                
        if i < len(charArray)-1:
            answer += "".join((charArray[i+1:]))
        elif i < len(numArray)-1:
            answer += "".join((numArray[i+1:]))

        return answer


        

        