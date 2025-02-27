class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        myMap = {} 
        for i in range(len(graph)):
            myMap[i] = graph[i]

        visitedIndex = set()  
        safeNode = {}  

        def function(index):
            if index in safeNode:  
                return safeNode[index]

            if myMap[index] == []:  
                safeNode[index] = True
                return True

            if index in visitedIndex: 
                safeNode[index] = False
                return False

            visitedIndex.add(index) 
            theList = myMap[index]
            isSafe = True  
            
            for i in range(len(theList)):
                ans = function(theList[i])
                if not ans:  
                    isSafe = False
                    break
            
            visitedIndex.remove(index)  

            safeNode[index] = isSafe 
            return isSafe

        for index in range(len(graph)):
            function(index)

        answer = [i for i in range(len(myMap)) if safeNode.get(i, False)]

        return answer
