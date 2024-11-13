# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        length = [0]
        self.recursion(root,0,length)
        answer = []
        for i in range(length[0]):
            answer.append(0)
        left = TreeNode(root.val, root.left, root.right)
        self.fillLeftSide(left,answer,0)
        self.fillRightSide(root,answer,0)
        return answer

    def fillLeftSide(self,root,answer,index):
        if root == None:
            return
        answer[index] = root.val
        index+=1
        self.fillLeftSide(root.left, answer, index)
        self.fillLeftSide(root.right,answer, index)

    def fillRightSide(self,root,answer,index):
        if root == None:
            return
        answer[index] = root.val
        index+=1
        self.fillRightSide(root.right,answer,index)

    def recursion(self,root,index,length):
        if root == None:
            return
        index+=1
        length[0] = max(length[0],index)
        self.recursion(root.left, index,length)
        self.recursion(root.right,index,length)