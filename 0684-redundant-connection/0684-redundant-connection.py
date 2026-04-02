class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parents = [i for i in range(len(edges) + 1)]
    
        def findParent(val):
            if parents[val] == val:
                return val
            parents[val] = findParent(parents[val])
            return parents[val]

        def union(first,second):
            xvalParent = findParent(first)
            yvalParent = findParent(second)
            if xvalParent == yvalParent:
                return True
            parents[yvalParent] = xvalParent
            return False

        for i in range(len(edges)):
            if union(edges[i][0],edges[i][1]) == True:
                return edges[i]