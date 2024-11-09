class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        hashMap = {}
        self.recursion(root,hashMap)
        max_frequency = max(hashMap.values(), default=0)
        modes = [key for key, freq in hashMap.items() if freq == max_frequency]
        return modes

    def recursion(self,root,hashMap):
        if root == None:
            return
        if root.val not in hashMap:
            hashMap[root.val] = 1
        elif root.val in hashMap:
            hashMap[root.val]+=1
        self.recursion(root.left, hashMap)
        self.recursion(root.right,hashMap)
        