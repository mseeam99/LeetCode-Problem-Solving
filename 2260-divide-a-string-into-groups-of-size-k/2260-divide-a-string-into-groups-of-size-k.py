class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        array = []
        tempString = ""
        
        for i in range(len(s)):
            tempString += s[i]
            if len(tempString) == k:
                array.append(tempString)
                tempString = ""
        
        if tempString:
            while len(tempString) < k:
                tempString += fill
            array.append(tempString)
        
        return array
