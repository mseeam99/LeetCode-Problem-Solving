class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        array = [0] * len(score)
        for i in range(len(score)):
            val = score[i] * -1
            index = i
            score[i] = (val,index)
        heapq.heapify(score)
        count = 0
        while score: 
            count += 1
            item = heapq.heappop(score)
            val = item[0]
            index = item[1]
            if count == 1:
                array[index] = "Gold Medal"
            elif count == 2:
                array[index] = "Silver Medal"
            elif count == 3:
                array[index] = "Bronze Medal"
            else:
                array[index] = str(count)
        return array