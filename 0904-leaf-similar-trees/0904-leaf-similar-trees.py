# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        rootOneValues = []
        rootTwoValues = []
        self.recursion(root1,rootOneValues)
        self.recursion(root2,rootTwoValues)
        if rootOneValues == rootTwoValues:
            return True
        else:
            return False
        
    def recursion(self,root,values):
        if root == None:
            return False
        left  = self.recursion(root.left, values)
        right = self.recursion(root.right,values)
        if left == False and right == False:
            values.append(root.val)