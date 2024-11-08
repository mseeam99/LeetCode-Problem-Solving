# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        answer = [True]
        self.recursion(root.left,root.right,answer)
        return answer[0]

    def recursion(self,rootOne,rootTwo,answer):

        if (rootOne == None and rootTwo != None) or (rootOne != None and rootTwo == None):
            answer[0] = False
            
        if answer[0] == False:
            return False

        if rootOne == None and rootTwo == None:
            return True
        
        if rootOne.val != rootTwo.val:
            answer[0] = False
            
        if answer[0] == False:
            return False

        self.recursion(rootOne.left,rootTwo.right,answer) 
        self.recursion(rootOne.right,rootTwo.left,answer)

        return True

        
