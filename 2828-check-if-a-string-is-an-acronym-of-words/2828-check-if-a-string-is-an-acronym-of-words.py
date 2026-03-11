class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        s = list(s)
        if len(s) != len(words):
            return False
        for i in range(len(words)):
            if i <= len(s)-1 and words[i][0] != s[i]:
                return False
        return True
        