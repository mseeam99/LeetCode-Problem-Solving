class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root.left is None and root.right is None:
            return root.val
        answer = []
        self.depthFirstSearch(root, 1, None, answer)
        max_depth = 0
        bottom_left_value = None
        for val, gotDepth, direction in answer:
            if gotDepth > max_depth:  
                max_depth = gotDepth
                bottom_left_value = val
            elif gotDepth == max_depth and bottom_left_value is None and direction == 0: 
                bottom_left_value = val
        return bottom_left_value

    def depthFirstSearch(self, root, depth, direction, answer):
        if root is None:
            return
        answer.append((root.val, depth, direction))
        self.depthFirstSearch(root.left, depth + 1, 0, answer)
        self.depthFirstSearch(root.right, depth + 1, 1, answer)
