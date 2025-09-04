class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        def binarySearch(potions,spellElement,success):
            left = 0
            right = len(potions)-1
            while left <= right:
                middle = left + (right-left) // 2
                multipliedValue = spellElement * potions[middle]
                if multipliedValue >= success:
                    right = middle - 1
                elif multipliedValue < success:
                    left = middle + 1
            return len(potions) - left


        potions.sort()
        answer = []

        for i in range(len(spells)):
            answer.append(binarySearch(potions,spells[i],success))
        
        return answer









        


