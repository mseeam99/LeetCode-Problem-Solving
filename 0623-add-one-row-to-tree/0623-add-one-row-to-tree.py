# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        if depth == 1:
            return TreeNode(val,root,None)

        queue = deque([root] if root else [])
        level = 1

        while len(queue) != 0:
            queueLength = len(queue)
            if level == depth - 1:
                for _ in range(queueLength):
                    current_node = queue.popleft()
                    current_node.left = TreeNode(val,current_node.left,None)
                    current_node.right = TreeNode(val,None,current_node.right)
                break
        
            for _ in range(queueLength):
                currentNode = queue.popleft()
                if currentNode.left != None:
                    queue.append(currentNode.left)
                if currentNode.right != None:
                    queue.append(currentNode.right)

            level += 1

        return root

        