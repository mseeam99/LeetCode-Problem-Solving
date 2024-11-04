# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        answer = [0]
        self.recursion(root,answer)
        return answer[0]

    def recursion(self,root,answer):

        if root == None:
            return 0

        left  = self.recursion(root.left, answer)
        right = self.recursion(root.right,answer)

        currentPathSum = (left+right)
        answer[0] = max(answer[0],currentPathSum)

        return max(left,right)+1

        

        