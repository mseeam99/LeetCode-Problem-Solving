class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        if len(s) < k:
            return "".join(list(s[::-1]))

        returnString = ""
        tempString = ""
        flag = 0
        index = 0

        while index < len(s):
            tempString = s[index:index+k]
            if flag % 2 == 0:
                returnString += tempString[::-1]
                tempString = ""
                flag += 1
            elif flag % 2 == 1:
                returnString += tempString
                tempString = ""
                flag += 1
            index += k
            
        return returnString