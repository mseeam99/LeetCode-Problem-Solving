class Solution:
    def digitSum(self, s: str, k: int) -> str:
        s = list(s)
        while len(s) > k:
            newString = ""
            for i in range(0,len(s),k):
                summationArray = s[i:i+k]
                summationValue = 0
                for i in range(len(summationArray)):
                    summationValue += int(summationArray[i])
                newString += str(summationValue)
            s = newString
        return "".join(s)










        