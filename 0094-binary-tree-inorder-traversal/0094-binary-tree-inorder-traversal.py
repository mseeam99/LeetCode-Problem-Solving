# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        array = []
        self.traverse(root,array)
        return array

    def traverse(self,root,array):
        if root == None:
            return
        self.traverse(root.left,array)
        array.append(root.val)
        self.traverse(root.right,array)



    

        