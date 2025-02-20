class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        myMap = {}
        visitedSet = set()

        for i in range(numCourses):
            if i not in myMap:
                myMap[i] = []
        for i in range(len(prerequisites)):
            myMap[prerequisites[i][1]].append(prerequisites[i][0])

        def function(c):
            if c in visitedSet:
                return False

            if myMap[c] == []:
                return True
            
            visitedSet.add(c)
            for pre in myMap[c]:
                if function(pre) == False:
                    return False
            visitedSet.remove(c)
            myMap[c] = []
            return True

        for i in range(len(prerequisites)):
            if function(prerequisites[i][1]) == False:
                return False

        return True

            






        
       

        