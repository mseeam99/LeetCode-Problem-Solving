class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        mySet = set()
        mySet.add(1)
        
        myHeap = [1]
        heapq.heapify(myHeap)

        count = 1

        while heapq:
            currentValue = heapq.heappop(myHeap)
            count += 1
            for item in [2,3,5]:    
                val = currentValue * item
                if val not in mySet:
                    heapq.heappush(myHeap,val)
                    mySet.add(val)
                    
                if count == n+1: 
                    return currentValue
       
            if count > n:
                break
            

       
            
            
        

    


        
            


        