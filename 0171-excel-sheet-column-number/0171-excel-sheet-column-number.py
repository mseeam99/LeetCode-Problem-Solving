class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        value = 0
        power = -1
        
        for i in range(len(columnTitle)-1,-1,-1):
            char_value = ord(columnTitle[i]) - 64
            power += 1
            value += char_value * (26 ** power)
        
        return value