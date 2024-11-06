# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        currentSum = [0]
        answer = [False]
        self.recursion(root,targetSum,answer,currentSum)
        return answer[0]

    def recursion(self,root,targetSum,answer,currentSum):
        if root == None:
            return True
        currentSum[0] = currentSum[0]+root.val
        self.recursion(root.left,targetSum,answer,currentSum)
        self.recursion(root.right,targetSum,answer,currentSum)
        if currentSum[0] == targetSum and root.left == None and root.right == None:
            answer[0] = True
            return True
        currentSum[0] = currentSum[0]-root.val