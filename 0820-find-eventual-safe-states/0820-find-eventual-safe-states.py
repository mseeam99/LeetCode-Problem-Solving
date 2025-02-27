class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        myMap = {}  # Mapping of index to its adjacent nodes
        for i in range(len(graph)):
            myMap[i] = graph[i]

        visitedIndex = set()  # To track nodes in the current path
        safeNode = {}  # To track the final safe/unsafe state of nodes

        def function(index):
            if index in safeNode:  # If already computed, return it
                return safeNode[index]

            if myMap[index] == []:  # No outgoing edges means it's a safe node
                safeNode[index] = True
                return True

            if index in visitedIndex:  # Detected a cycle
                safeNode[index] = False
                return False

            visitedIndex.add(index)  # Mark as visited in the current path
            theList = myMap[index]
            isSafe = True  # Assume it's safe unless proven otherwise
            
            for i in range(len(theList)):
                ans = function(theList[i])
                if not ans:  # If any neighbor is not safe, mark this node unsafe
                    isSafe = False
                    break
            
            visitedIndex.remove(index)  # Remove from current path

            safeNode[index] = isSafe  # Record whether this node is safe or not
            return isSafe

        # Compute safety for each node in the graph
        for index in range(len(graph)):
            function(index)

        # Collect all safe nodes (those that have a True value in safeNode)
        answer = [i for i in range(len(myMap)) if safeNode.get(i, False)]

        return answer
