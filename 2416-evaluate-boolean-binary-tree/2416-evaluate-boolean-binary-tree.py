# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        self.recursion(root)
        if root.val == 0:
            return False
        else:
            return True
        
    def recursion(self,root):
        if root == None:
            return 0

        left  = self.recursion(root.left)
        right = self.recursion(root.right)

        if root.val == 2:
            root.val = left | right
        elif root.val == 3:
            root.val = left & right
      
        return root.val

        
