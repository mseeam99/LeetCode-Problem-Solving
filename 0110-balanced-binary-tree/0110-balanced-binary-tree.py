# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        answer = [True]
        self.recursion(root,answer)
        return answer[0]
        

    def recursion(self,root,answer):

        if root == None:
            return 0

        left  = self.recursion(root.left, answer)
        right = self.recursion(root.right,answer)

        if abs(left-right)>=2:
            answer[0] = False

        if answer[0] == False:
            return False
        
        return max(left, right) + 1

     
