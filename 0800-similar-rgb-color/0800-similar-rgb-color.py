class Solution:
    def similarRGB(self, color: str) -> str:
        

        def getVal(s):
            minValue = float("inf")
            ans = -1
            for i in range(16):
                currValue = ((int(s,16) - (i*17))**2)
                if currValue < minValue:
                    minValue = currValue
                    ans = i
            
            return hex(ans)[-1]
            



        answer = "#"
        for i in range(1,6,2):
            answer += getVal(color[i:i+2])
        return answer