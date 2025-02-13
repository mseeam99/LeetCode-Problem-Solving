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
     

        return gotIt

        

            
                
        