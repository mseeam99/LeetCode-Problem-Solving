class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        i = 0
        j = 0

        answer = []

        while i < len(firstList) and j < len(secondList):

            firstStart = firstList[i][0]
            firstEnd = firstList[i][1]

            secondStart = secondList[j][0]
            secondEnd = secondList[j][1]

            start = max(firstStart,secondStart)
            end = min(firstEnd,secondEnd)

            if start <= end:
                answer.append([start,end])

            if firstEnd < secondEnd:
                i += 1
            else:
                j += 1

        return answer

            

        