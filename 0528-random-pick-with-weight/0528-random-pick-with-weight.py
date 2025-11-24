import random
class Solution:
    def __init__(self, w: List[int]):
        self.weightCumilative = [0]*len(w)
        self.total = 0
        for i in range(len(w)):
            self.total += w[i]
            self.weightCumilative[i] = self.total
        print(self.weightCumilative[i])
        return None
    
    def binarySearch(self,val):
        left = 0
        right = len(self.weightCumilative)-1
        while left <= right:
            middle = left + (right-left) // 2
            if self.weightCumilative[middle] == val:
                return middle
            elif self.weightCumilative[middle] < val:
                left = middle + 1
            else:
                right = middle - 1
        return left

    def pickIndex(self) -> int:
        randomNumber = random.randint(1,self.total)
        answerIndex = self.binarySearch(randomNumber)
        return answerIndex

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()