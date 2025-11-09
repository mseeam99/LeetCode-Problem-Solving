class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def checkHIndex(idx):
            count = 0
            for i in range(len(citations)):
                if citations[i] >= idx:
                    count+=1
            return True if count>=idx else False
        left = 0
        right = max(citations)
        while left<=right:
            middle = left + (right-left) // 2
            if checkHIndex(middle) == True:
                left = middle + 1
            else:
                right = middle - 1
        return left - 1

        