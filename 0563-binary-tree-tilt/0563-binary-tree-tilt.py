class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total_tilt = 0
        self.calculate_sum(root)
        return self.total_tilt
    
    def calculate_sum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_sum = self.calculate_sum(root.left)
        right_sum = self.calculate_sum(root.right)
        current_tilt = abs(left_sum - right_sum)
        self.total_tilt += current_tilt
        return root.val + left_sum + right_sum
