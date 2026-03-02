class Solution:
    def reverseByType(self, s: str) -> str:

        s = list(s)
       
        lowerCaseArray = []
        speciaArray = []

        for i in range(len(s)):
            if "a" <= s[i] <= "z":
                lowerCaseArray.append(s[i])
            else:
                speciaArray.append(s[i])

        for i in range(len(s)):
            if "a" <= s[i] <= "z":
                s[i] = lowerCaseArray.pop()
            else:
                s[i] = speciaArray.pop()



        

        return "".join(s)
        