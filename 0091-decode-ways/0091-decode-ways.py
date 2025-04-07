class Solution:
    def numDecodings(self, s: str) -> int:

        if not s or s[0] == '0':  
            return 0

        array = [0] * (len(s)+1)
        array[0] = 1  
        array[1] = 1 

        for i in range(2,len(s)+1):
            if int(s[i-1]) != 0 and int(s[i-1]) >= 1 and int(s[i-1]) <= 9:
                array[i] += int(array[i-1])

            getDoubleDigitNumber = s[i-2:i]
            
            if (int(getDoubleDigitNumber) >= 10 and int(getDoubleDigitNumber) <= 26):
                array[i] += int(array[i-2])

        return array[-1]
            


        
       

        