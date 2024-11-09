class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        array = []
        self.recursion(root,k,array)
        array.sort()
        left = 0
        right = len(array)-1
        while left < right:
            if array[left] + array[right] < k:
                left+=1
            elif array[left] + array[right] > k:
                right-=1
            elif array[left] + array[right] == k:
                return True
        return False
        
    def recursion(self,root,k,array):
        if root == None:
            return
        array.append(root.val)
        self.recursion(root.left,k,array)
        self.recursion(root.right,k,array)

        