# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        array = []
        self.recursion(root,array,"")
        return array

    def recursion(self,root,array,string):
        if root == None:
            return False

        string += str(root.val)
        string += "->"

        left  = self.recursion(root.left,array,string)
        right = self.recursion(root.right,array,string)

        if left == False and right == False:
            string = string[:len(string)-2]
            array.append(string)
        