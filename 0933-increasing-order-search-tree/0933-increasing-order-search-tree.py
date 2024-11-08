# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        array = []
        self.collectEveryElement(root,array)
        array.sort()
        print(array)
        index = 0
        newRoot = self.makeTree(root,array,index)
        return newRoot

    def makeTree(self,root,array,index):
        if index >= len(array):
            return
        root = TreeNode()
        root.val = array[index]
        index+=1
        root.right = self.makeTree(TreeNode(),array,index)
        return root

    def collectEveryElement(self,root,array):
        if root == None:
            return
        array.append(root.val)
        self.collectEveryElement(root.left, array)
        self.collectEveryElement(root.right,array)
        