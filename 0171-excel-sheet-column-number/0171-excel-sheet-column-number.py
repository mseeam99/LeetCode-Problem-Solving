class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        n = len(columnTitle)
        value = 0
        
        for i in range(n):
            char_value = ord(columnTitle[i]) - 64
            power = n - i - 1
            
            value += char_value * (26 ** power)
        
        return value