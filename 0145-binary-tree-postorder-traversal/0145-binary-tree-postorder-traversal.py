# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        array = []
        self.traverse(root,array)
        return array

    def traverse(self,root,array):
        
        if root == None:
            return
        
        self.traverse(root.left,array)
        self.traverse(root.right,array)
        array.append(root.val)



        
        