class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

     
        for i in range(len(stones)):
            stones[i] = (stones[i]*(-1))

        heapq.heapify(stones)

        while stones:

            print(stones)

            if len(stones) == 1:
                return stones[0]*-1
                
            if stones:
                x = heapq.heappop(stones)
                x = x * (-1)
            if stones:
                y = heapq.heappop(stones)
                y = y * (-1)
            
            if x == y:
                continue
            else:
                newWeight = abs(y-x)
                heapq.heappush(stones,newWeight*(-1))

        return 0





            
        
        