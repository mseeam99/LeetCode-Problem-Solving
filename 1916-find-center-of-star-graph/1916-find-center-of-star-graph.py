class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        first  = edges[0][0]
        second = edges[0][1]

        gotIt = -100


        for i in range(1,2):
            if edges[i][0] == first:
                gotIt = first
            elif edges[i][1] == first:
                gotIt = first
            elif edges[i][0] == second:
                gotIt = second
            elif edges[i][1] == second:
                gotIt = second
        
        count = len(edges) - 2
        i = 0
        for i in range(2,len(edges)):
            if gotIt in edges[i]:
                i+=1
        
        if i == count:
            return gotIt

        return gotIt

        

            
                
        