from collections import deque

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        cloned = {node: Node(node.val, [])}
        queue = deque([node])

        while queue:
            cur = queue.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in cloned:
                    cloned[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                cloned[cur].neighbors.append(cloned[neighbor])

        return cloned[node]
