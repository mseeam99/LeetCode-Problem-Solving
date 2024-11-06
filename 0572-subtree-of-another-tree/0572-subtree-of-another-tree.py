class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (root == None or subRoot == None):
            return False
       
        answer = [False]
        self.findSameValue(root,subRoot,answer)
        return answer[0]

    def findSameValue(self,root,subRoot,answer):
        if root == None and subRoot == None:
            return True

        if root == None or subRoot == None:
            return False
       
        if root.val == subRoot.val:
            if self.recursion(root, subRoot, answer) == True:
                answer[0] = True
                return answer[0]
        
        self.findSameValue(root.left,subRoot,answer)
        self.findSameValue(root.right,subRoot,answer)

    def recursion(self,root,subRoot,answer):
        if root == None and subRoot == None:
            return True
        if root == None or subRoot == None:
            return False
        if (root.val != subRoot.val):
            return False
        left  = self.recursion(root.left,  subRoot.left, answer)
        right = self.recursion(root.right, subRoot.right, answer)
        return left and right


        