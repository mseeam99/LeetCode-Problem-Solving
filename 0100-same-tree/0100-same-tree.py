# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        answer = [True]
        self.recursion(p,q,answer)
        return answer[0]

    def recursion(self,one,two,answer):
        
        if one == None and two == None:
            return 

        if one == None and two != None:
            answer[0] = False 
            return
            
        if one != None and two == None:
            answer[0] = False 
            return
            
        if one.val != two.val:
            answer[0] = False
        
        if answer[0] == False:
            return False
            
        self.recursion(one.left,two.left,answer)
        self.recursion(one.right,two.right,answer)