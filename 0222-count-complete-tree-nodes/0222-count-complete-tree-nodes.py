# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count = [0]
        self.recursion(root,count)
        return count[0]

    def recursion(self,root,count):
        if root == None:
            return
        count[0] = count[0] + 1
        self.recursion(root.left,count)
        self.recursion(root.right,count)


        