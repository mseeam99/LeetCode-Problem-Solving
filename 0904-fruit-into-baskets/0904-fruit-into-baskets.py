class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        leftPointer = 0
        rightPointer = 0

        hashMap = {}
        maxLength = 0

        while rightPointer <= len(fruits)-1:

            if fruits[rightPointer] not in hashMap:
                hashMap[fruits[rightPointer]] = 1
            else:
                hashMap[fruits[rightPointer]] += 1

            rightPointer += 1

            while len(hashMap) > 2:
                if fruits[leftPointer] in hashMap:
                    hashMap[fruits[leftPointer]] -= 1
                    if hashMap[fruits[leftPointer]] == 0:
                        del hashMap[fruits[leftPointer]] 
                leftPointer += 1
            

            maxLength = max(maxLength, rightPointer-leftPointer + 1)
        

        return maxLength-1


        