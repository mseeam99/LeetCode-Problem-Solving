from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        myMap = {}
        for i in range(numCourses):
            myMap[i] = []
        for i in range(len(prerequisites)):
            myMap[prerequisites[i][1]].append(prerequisites[i][0])

        visitedSet = set()  
        toReturn = []  

        def function(crs):
            # Detected a cycle
            if crs in visitedSet:
                return False


            visitedSet.add(crs)
            for nextCrs in myMap[crs]:
                if nextCrs not in toReturn:  
                    if not function(nextCrs):
                        return False
            visitedSet.remove(crs)
            toReturn.append(crs)  
            return True

        for i in range(numCourses):
            if i not in toReturn:
                if not function(i):
                    return []  

        return toReturn[::-1]
