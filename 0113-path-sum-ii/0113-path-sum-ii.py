# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        totalAnswer = []

        def recursion(root,currentSum,currentArray):
            if root == None:
                return

            currentSum += root.val
            currentArray.append(root.val)
            
            if root.left == None and root.right == None and currentSum == targetSum:
                totalAnswer.append(currentArray[:])

            recursion(root.left,currentSum,currentArray)
            recursion(root.right,currentSum,currentArray)

            currentArray.pop()
            
        recursion(root,0,[])
        return totalAnswer

        