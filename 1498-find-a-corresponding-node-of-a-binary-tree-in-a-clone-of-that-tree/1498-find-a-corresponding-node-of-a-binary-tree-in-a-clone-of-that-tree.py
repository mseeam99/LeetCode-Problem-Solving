# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        tempNodeValue = [None]
        answer = [None]
        self.getTheValue(original,target,tempNodeValue)
        self.recursion(cloned,target,answer)
        return answer[0]

    def getTheValue(self,original,target,tempNodeValue):
        if original == None:
            return
        if original.val == target.val:
            tempNodeValue[0] = target.val
            return
        self.getTheValue(original.left, target,tempNodeValue)
        self.getTheValue(original.right,target,tempNodeValue)

    def recursion(self,root,target,answer):
        if root == None:
            return
        if root.val == target.val:
            answer[0] = root
            return
        self.recursion(root.left, target,answer)
        self.recursion(root.right,target,answer)

        