class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:

        weight.sort()
        count = 0
        unites = 0

        for i in range(len(weight)):
            unites += weight[i]
            if unites <= 5000:
                count += 1
            else:
                break
        


        return count

        