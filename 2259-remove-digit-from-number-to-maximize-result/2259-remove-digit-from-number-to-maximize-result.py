class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        for i in range(len(number)-1):
            if number[i] == digit and number[i+1]>digit:
                return number[:i] + number[i+1:]
        lastidx = 0
        for i in range(len(number)-1,-1,-1):
            if number[i] == digit:
                lastidx = i
                break
        
        return number[:lastidx] + number[lastidx+1:]
                
        
            



                

        