# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        finalString = [""]
        self.depthFirstSearch(root,finalString,"")
        return finalString[0]

    def depthFirstSearch(self,root,finalString,currentString):
        if root == None:
            return
        currentString += (chr(ord('a') + root.val))
        if root.left == None and root.right == None:
            currentString = currentString[::-1]
            if finalString[0] == "" or currentString < finalString[0]:
                finalString[0] = currentString
        self.depthFirstSearch(root.left,finalString,currentString)
        self.depthFirstSearch(root.right,finalString,currentString)

        


        