class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = [0] * n
        for u, v in edges:
            incoming[v] += 1

        result = []
        for i in range(n):
            if incoming[i] == 0:
                result.append(i)
                
        return result
