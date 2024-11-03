# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxDepth = [0]
        depth = 0
        self.traverse(root,depth,maxDepth)
        return maxDepth[0]
    
    def traverse(self,root,depth,maxDepth):
        if root == None:
            return
        depth+=1
        maxDepth[0] = max(depth,maxDepth[0])
        self.traverse(root.left,depth,maxDepth)
        self.traverse(root.right,depth,maxDepth)
        depth-=1
        
        
