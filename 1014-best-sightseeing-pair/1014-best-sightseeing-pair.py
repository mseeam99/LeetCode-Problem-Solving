class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        leftMaxScore = values[0] + 0
        maxAnswer = 0


        for j in range(1,len(values)):

            maxAnswer = max(maxAnswer, leftMaxScore + values[j]-j)


            leftMaxScore = max(leftMaxScore, values[j]+j)

            

        return maxAnswer




        

        