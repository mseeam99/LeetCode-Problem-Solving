# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        maxWidth = 0
        root.val = 1
        level = 1
        myQueue = deque([(root,root.val,level)] if root else None)
        while len(myQueue) != 0:
            currentNode,currentValue,level = myQueue.popleft()
            if currentNode.left != None:
                myQueue.append((currentNode.left,(2 * currentValue),level+1))
            if currentNode.right != None:
                myQueue.append((currentNode.right,((2 * currentValue) + 1),level+1))
            lowerstValue  = 0
            heightstValue = 0

            for i, value in enumerate(myQueue):
                if myQueue[0][2] == myQueue[len(myQueue)-1][2]:
                    if i == 0:
                        lowerstValue = myQueue[i][1]
                    if i == len(myQueue)-1 :
                        heightstValue = myQueue[len(myQueue)-1][1]
            maxWidth = max(maxWidth,(heightstValue-lowerstValue)+1)

        return maxWidth
            











        