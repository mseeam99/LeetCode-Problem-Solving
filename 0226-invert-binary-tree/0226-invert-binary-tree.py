# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invert(root)
        return root
        
    def invert(self,root):
        
        if root == None:
            return

        self.invert(root.left)
        self.invert(root.right)
        root.left, root.right = root.right, root.left