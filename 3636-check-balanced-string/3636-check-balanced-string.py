class Solution:
    def isBalanced(self, num: str) -> bool:
        summ = 0
        even = 0
        for i in range(len(num)):
            if i % 2 == 0:
                summ = summ + int(num[i])
            else:
                even = even + int(num[i])
        return summ == even




        