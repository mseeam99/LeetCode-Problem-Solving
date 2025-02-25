class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        length = len(isConnected)

        myMap = {}
        for i in range(length):
            myMap[i] = []

        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    myMap[i].append(j)

        visitedSet = set()

        answer = 0

        def recursion(key):

            nonlocal answer 

            if myMap[key] == [key]:
                return True

            if (key) in visitedSet:
                return True

            
            visitedSet.add((key))

            theList = myMap[key]
            for i in theList:
                recursion(i)
           
            return True

        

        for i in range(length):
            if (i) not in visitedSet and recursion(i) == True:
                answer+=1

        return answer



        



        