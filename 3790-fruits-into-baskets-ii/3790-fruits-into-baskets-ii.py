class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:

        used = [False] * len(baskets)
        count = 0

        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if baskets[j] >= fruits[i] and used[j] == False:
                    used[j] = True
                    count+=1
                    break
               
        return len(fruits) - count

        
        