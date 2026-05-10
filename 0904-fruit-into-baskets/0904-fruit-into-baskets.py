class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        leftPointer = 0
        rightPointer = 0
        hashMap = {}
        maxFruitNumber = float("-inf")
        while rightPointer <= len(fruits)-1:
            if fruits[rightPointer] not in hashMap:
                hashMap[fruits[rightPointer]] = 1
            else:
                hashMap[fruits[rightPointer]] += 1
            while len(hashMap)>2:
                hashMap[fruits[leftPointer]] -= 1
                if hashMap[fruits[leftPointer]] == 0:
                    del hashMap[fruits[leftPointer]]
                leftPointer += 1
            maxFruitNumber = max(maxFruitNumber, rightPointer-leftPointer + 1)
            rightPointer += 1
        return maxFruitNumber



                







