class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        value = 0
        for i in range(len(columnTitle)):
            char = columnTitle[i]
            value = value * 26 + (ord(char) - 64)
        
        return value