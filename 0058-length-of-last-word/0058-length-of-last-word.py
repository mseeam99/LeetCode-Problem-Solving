class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in range(len(s)-1,-1,-1):
            if s[i].isalnum() == True:
                count+=1
            elif count != 0 and s[i].isalnum() == False:
                return count
        return count        