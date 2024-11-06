# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.recursion(nums,0,len(nums)-1)

    def recursion(self,nums,left,right):
        if left > right:
            return
        middleElement = (left + right) // 2
        root = TreeNode(nums[middleElement])
        root.left = self.recursion(nums,left,middleElement-1)
        root.right = self.recursion(nums,middleElement+1,right)
        return root
        