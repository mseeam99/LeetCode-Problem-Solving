# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        value = [0]
        value[0] = root.val
        answer = [True]
        self.recursion(root,value,answer)
        return answer[0]

    def recursion(self,root,value,answer):
        if root == None:
            return

        if root.val != value[0]:
            answer[0] = False
            return
        
        if answer[0] == False:
            return False
        
        self.recursion(root.left,value,answer)
        self.recursion(root.right,value,answer)

        