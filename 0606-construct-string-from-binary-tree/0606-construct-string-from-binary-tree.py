class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        answer = [""]
        self.recursion(root,answer)
        return answer[0]

    def recursion(self,root,answer):

        if root == None:
            return ""

        answer[0] = answer[0] + str(root.val)

        if root.left is not None:
            answer[0] = answer[0] + "("
            self.recursion(root.left,answer)
            answer[0] = answer[0] + ")"

        elif root.right is not None:
            answer[0] += "()"
        
        if root.right is not None:
            answer[0] = answer[0] + "("
            self.recursion(root.right,answer)
            answer[0] = answer[0] + ")"

        return answer[0]