class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:

        values = []        
        pointerLeft  = 0
        currSum = 0

        while pointerLeft < len(s):
            w = widths[ord(s[pointerLeft]) - ord('a')]
            if currSum + w > 100:
                values.append(currSum)
                currSum = 0
            currSum += w
            pointerLeft+=1
        
        values.append(currSum)
        return [len(values),values[-1]]