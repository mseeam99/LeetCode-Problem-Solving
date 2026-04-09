class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        dp = []
        for i in range(len(triangle)):
            tempArray = [0] * len(triangle[i])
            dp.append(tempArray)
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                dp[i][j] = 0
        dp[0][0] = triangle[0][0]

        for i in range(len(dp)):
            print(dp[i])









        for i in range(1,len(triangle)):

            for j in range(len(triangle[i])):

                if i-1 >= 0 and i-1 <= len(triangle)-1 and j >= 0 and j <= len(triangle[i-1])-1:
                    straightUp = dp[i-1][j]
                else:
                    straightUp = float("inf")

                if i-1 >= 0 and i-1 <= len(triangle)-1 and j-1 >= 0 and j-1 <= len(triangle[i-1])-1:
                    rightSidUp =  dp[i-1][j-1]
                else:
                    rightSidUp =  float("inf")

                minPath = triangle[i][j] + min(straightUp,rightSidUp)

                dp[i][j] = minPath
                

        print()
        for i in range(len(dp)):
            print(dp[i])

        return min(dp[-1])


        