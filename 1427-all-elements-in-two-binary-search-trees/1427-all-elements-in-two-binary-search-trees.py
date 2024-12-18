# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        answer = []
        self.dfs(root1,answer)
        self.dfs(root2,answer)
        answer.sort()
        return answer

    def dfs(self,root,answer):
        if root == None:
            return
        answer.append(root.val)
        self.dfs(root.left,answer)
        self.dfs(root.right,answer)




        