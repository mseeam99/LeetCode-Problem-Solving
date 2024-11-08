# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        array = []
        self.recursion(root,array)
        array.sort()
        answer = float('inf')
        for i in range(len(array)-1):
            currentDifference = array[i+1] - array[i]
            if currentDifference <= answer:
                answer = currentDifference
        return answer

    def recursion(self,root,array):
        if root == None:
            return
        array.append(root.val)
        self.recursion(root.left,array)
        self.recursion(root.right,array)