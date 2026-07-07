class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        mySet = set()
        for i in range(len(triplets)):
            theArray = triplets[i]
            if theArray[0] > target[0] or theArray[1] > target[1] or theArray[2] > target[2]:
                continue
            for index in range(len(theArray)):
                if theArray[index] == target[index]:
                    mySet.add(index)
        if len(mySet) == 3:
            return True
        return False

            

        