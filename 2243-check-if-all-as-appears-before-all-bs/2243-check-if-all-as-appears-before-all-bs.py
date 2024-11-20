class Solution:
    def checkString(self, s: str) -> bool:
        for i in range(len(s)):
            if s[i] == "b":
                tempString = s[i:]
                if "a" in tempString:
                    return False
        return True