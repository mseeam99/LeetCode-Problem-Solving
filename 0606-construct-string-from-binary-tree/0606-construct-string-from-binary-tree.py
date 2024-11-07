class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        return self.recursion(root)
    
    def recursion(self, root):
        if root is None:
            return ""
        
        result = str(root.val)
        
        if root.left or root.right: 
            result += "(" + str(self.recursion(root.left)) + ")"
        
        if root.right != None:
            result += "(" + str(self.recursion(root.right)) + ")"
        
        return result
