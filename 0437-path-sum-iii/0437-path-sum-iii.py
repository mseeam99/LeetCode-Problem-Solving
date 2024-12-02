class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        answer = [0] 
        self.recursion(root, answer, targetSum)
        return answer[0]

    def recursion(self, root, answer, targetSum):
        if root is None:
            return
        self.checkPathSum(root,0,targetSum,answer)
        self.recursion(root.left, answer, targetSum)
        self.recursion(root.right, answer, targetSum)
        
    def checkPathSum(self, root, currentSum, targetSum, answer):
        if root is None:
            return
        currentSum += root.val
        if currentSum == targetSum:
            answer[0] += 1
        self.checkPathSum(root.left,currentSum,targetSum,answer)
        self.checkPathSum(root.right,currentSum,targetSum,answer)
      