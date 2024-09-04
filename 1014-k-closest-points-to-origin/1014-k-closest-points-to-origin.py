import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        listOfAnswers = []
        for i in range(len(points)):
            listOfAnswers.append(((points[i][0] ** 2) + (points[i][1] ** 2),points[i]))
        topKelements = heapq.nsmallest(k,listOfAnswers)
        for i in range(k):
            topKelements[i] = topKelements[i][1]
        return topKelements


        

        