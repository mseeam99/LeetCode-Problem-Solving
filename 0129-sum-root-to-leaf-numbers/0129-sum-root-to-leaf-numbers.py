# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        answer = []
        self.depthFirstSearch(root,"",answer)
        finalAnswer = 0
        for i in range(len(answer)):
            finalAnswer+=int(answer[i])
        return finalAnswer

    def depthFirstSearch(self,root,string,answer):
        if root == None:
            return None
        string += str(root.val)
        left  = self.depthFirstSearch(root.left,string,answer)
        right = self.depthFirstSearch(root.right,string,answer)
        if left == None and right == None:
            answer.append(int(string))
            return True
        return True