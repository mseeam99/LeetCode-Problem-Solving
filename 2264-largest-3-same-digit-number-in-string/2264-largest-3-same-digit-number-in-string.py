class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxFound = 0
        threeFound = False
        for i in range(len(num)-2):
            if num[i] == num[i+1] and num[i+1] == num[i+2]:
                threeFound = True
                maxFound = max(maxFound,int(num[i]))
        if threeFound == True:
            return str(maxFound)*3
        else:
            return ""