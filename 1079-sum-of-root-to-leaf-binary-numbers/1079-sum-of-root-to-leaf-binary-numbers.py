# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        array = []
        print(array)
        self.recursion(root,array,"")
        return sum(int(num, 2) for num in array)

    def recursion(self,root,array,string):
        if root == None:
            return False
        string += str(root.val)   
        left  = self.recursion(root.left,array,string)
        right = self.recursion(root.right,array,string)  
        if left == False and right == False:
            array.append(string)
        return True

        
        