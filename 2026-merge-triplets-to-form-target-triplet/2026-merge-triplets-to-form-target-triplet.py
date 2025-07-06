class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        theSet = [0,0,0]

        for i in triplets:

            if i[0] > target[0] or i[1] > target[1] or i[2] > target[2]:
                continue
            
            if i[0] == target[0]:
                theSet[0] = i[0]
            if i[1] == target[1]:
                theSet[1] = i[1]
            if i[2] == target[2]:
                theSet[2] = i[2]

            if theSet == target:
                return True

        return False

