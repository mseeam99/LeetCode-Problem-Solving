# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        answer = [None]
        self.recursion(root,val,answer)
        return answer[0]
       
    def recursion(self,root,value,answer):
        if root == None:
            return 

        if root.val == value:
            answer[0] = root
            return answer[0]
        
        self.recursion(root.left,  value,answer)
        self.recursion(root.right, value,answer)