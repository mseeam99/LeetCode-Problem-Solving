# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        answer = [float("inf")]
        self.recursion(root,answer,0)
        return answer[0]

    def recursion(self,root,answer,count):
        if root == None:
            return False
        count+=1
        left  = self.recursion(root.left,answer,count)
        right = self.recursion(root.right,answer,count)
        if left == False and right == False:
            min_value = min(count,answer[0])
            if min_value <= answer[0]:
                answer[0] = min_value
        