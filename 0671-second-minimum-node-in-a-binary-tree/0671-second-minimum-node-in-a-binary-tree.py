# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        array = []
        self.recursion(root,array)
        array.sort()
        firstValue = array[0]
        answer = -1
        for i in range(len(array)):
            if array[i] != firstValue:
                answer = array[i]
                break
        return answer

    def recursion(self,root,array):
        if root == None:
            return
        array.append(root.val)
        self.recursion(root.left,array)
        self.recursion(root.right,array)