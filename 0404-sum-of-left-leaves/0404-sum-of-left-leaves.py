# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        answer = [0]
        self.recursion(root,answer,False)
        return answer[0]

    def recursion(self,root,answer,booleanIsLeft):
        
        if root == None:
            return 
        
        if root.left == None and root.right == None and booleanIsLeft == True:
            answer[0] += root.val

        self.recursion(root.left, answer, True)
        self.recursion(root.right,answer, False)

        


        