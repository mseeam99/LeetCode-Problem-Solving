class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        currentString = ""
        for i in range(len(words)):
            currentString += words[i]
            if currentString != s[:len(currentString)]:
                return False
            if currentString == s:
                return True
        return False
            



        


        