# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        result = 0
        myQueue = deque([[root,1]] if root else [])

        while len(myQueue) != 0:
           
            firstValue = myQueue[0][1]
            lastValue = myQueue[-1][1]
            result = max(result, lastValue - firstValue + 1)
            
            for _ in range(len(myQueue)):
                currentNode,currentValue = myQueue.popleft()
                if currentNode.left != None:
                    myQueue.append([currentNode.left,(2*currentValue)])
                if currentNode.right != None:
                    myQueue.append([currentNode.right,(2*currentValue)+1])
            
        return result