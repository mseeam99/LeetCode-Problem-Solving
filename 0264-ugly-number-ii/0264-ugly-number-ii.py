class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        mySet = set()
        mySet.add(1)
        
        myHeap = [1]
        heapq.heapify(myHeap)

        count = 0

        while heapq:

            count += 1

            currentValue = heapq.heappop(myHeap)
            for item in [2,3,5]:    
                val = currentValue * item
                if val not in mySet:
                    heapq.heappush(myHeap,val)
                mySet.add(val)
            
            if count > n:
                break
            

        myList = list(mySet)
        print(myList)
        myList.sort()
        return myList[n-1]
            
                
            
            
        

    


        
            


        