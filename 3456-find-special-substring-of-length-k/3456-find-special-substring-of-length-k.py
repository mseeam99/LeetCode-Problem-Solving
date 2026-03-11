class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        s = list(s)
        for i in range(len(s) - k + 1):
            currentSubString = s[i:i+k]
            if currentSubString.count(currentSubString[0]) == len(currentSubString):
                if (i == 0 or currentSubString[0] != s[i-1]) and (i+k == len(s) or currentSubString[-1] != s[i+k]):
                    return True
        return False

        


        

        
        