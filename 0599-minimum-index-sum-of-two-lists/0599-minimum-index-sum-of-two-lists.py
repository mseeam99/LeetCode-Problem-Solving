class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        hashMap = {}

        for i in range(len(list1)):
            if list1[i] not in hashMap:
                hashMap[list1[i]] = [i]

        for i in range(len(list2)):
            if list2[i] not in hashMap:
                hashMap[list2[i]] = [i]
            else:
                hashMap[list2[i]].append(i)

        leastSum = float("inf")
        for key, val in hashMap.items():
            arrayOfIndices = val
            summation = 0
            if len(arrayOfIndices) == 2:
                summation = arrayOfIndices[0] + arrayOfIndices[1]
                leastSum = min(leastSum,summation)

        answer = []
        for key, val in hashMap.items():
            arrayOfIndices = val
            if len(arrayOfIndices) == 2:
                if leastSum == arrayOfIndices[0] + arrayOfIndices[1]:
                    answer.append(key)

        return answer


        
           