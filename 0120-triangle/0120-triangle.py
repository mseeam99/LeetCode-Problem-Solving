class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev = [0] * len(triangle[0])
        prev[0] = triangle[0][0]
        for i in range(1,len(triangle)):
            temp = [0] * len(triangle)
            for j in range(len(triangle[i])):
                if i-1 >= 0 and i-1 <= len(triangle)-1 and j >= 0 and j <= len(triangle[i-1])-1:
                    straightUp = prev[j]
                else:
                    straightUp = float("inf")
                if i-1 >= 0 and i-1 <= len(triangle)-1 and j-1 >= 0 and j-1 <= len(triangle[i-1])-1:
                    rightSidUp =  prev[j-1]
                else:
                    rightSidUp =  float("inf")
                minPath = triangle[i][j] + min(straightUp,rightSidUp)
                temp[j] = minPath
            prev = temp
        return min(prev)


        