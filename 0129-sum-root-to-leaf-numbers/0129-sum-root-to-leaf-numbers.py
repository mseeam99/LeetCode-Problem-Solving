# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        answer = [0]
        tempString = ""
        self.recursion(root,tempString,answer)
        return answer[0]

    def recursion(self,root,tempString,answer):
        if root == None:
            return False
        tempString += str(root.val)
        left  = self.recursion(root.left,tempString,answer)
        right = self.recursion(root.right,tempString,answer)
        if left == False and right == False:
            print(int(tempString))
            answer[0] += int(tempString)
        return True

        