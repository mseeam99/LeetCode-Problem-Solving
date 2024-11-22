# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        myQueue = deque([root] if root else [])
        while len(myQueue) != 0:
            tempArray = []
            for i in range(len(myQueue)):
                currentNode = myQueue.popleft()
                tempArray.append(currentNode.val)
                if currentNode.left != None:
                    myQueue.append(currentNode.left)
                if currentNode.right != None:
                    myQueue.append(currentNode.right)
            if len(result) % 2 != 0:
                tempArray = tempArray[::-1]
            result.append(tempArray)
        return result
                


        