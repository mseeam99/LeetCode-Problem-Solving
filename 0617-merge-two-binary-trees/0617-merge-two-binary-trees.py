class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.recursion(root1,root2)
    
    def recursion(self,root1,root2):

        if root1 == None and root2 == None:
            return None

        newTree = TreeNode(0)

        if root1 != None and root2 == None:
            newTree.val = root1.val 
        elif root1 == None and root2 != None:
            newTree.val = root2.val
        else:
            newTree.val = root1.val + root2.val

        newTree.left = self.recursion(root1.left if root1 else None, root2.left if root2 else None)
        newTree.right = self.recursion(root1.right if root1 else None, root2.right if root2 else None)
        
        return newTree

        