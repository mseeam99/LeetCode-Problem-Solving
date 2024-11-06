# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = [0]
        self.recursion(root,low,high,result)
        return result[0]

    def recursion(self,root,low,high,result):
        if root == None:
            return 

        if (root.val >= low) and (root.val <= high):
            result[0] = result[0] + root.val
        
        self.recursion(root.left,low,high,result)
        self.recursion(root.right,low,high,result)
        