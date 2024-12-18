# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        theDepth = self.breadthFirstSearchGetMaxDepth(root)
        answer = [0]
        self.breadthFirstSearchToSum(root,theDepth,answer)
        return answer[0]

    def breadthFirstSearchToSum(self,root,theDepth,answer):
        myQuque = deque([(root,1)] if root else None)
        while len(myQuque) != 0:
            currentNode,index = myQuque.popleft()
            if index == theDepth:
                answer[0]+=currentNode.val
            if currentNode.left != None:
                myQuque.append((currentNode.left,index+1))
            if currentNode.right != None:
                myQuque.append((currentNode.right,index+1))

    def breadthFirstSearchGetMaxDepth(self,root):
        myQuque = deque([(root,1)] if root else None)
        lastToResturn = 1
        while len(myQuque) != 0:
            currentNode,index = myQuque.popleft()
            lastToResturn = max(index,lastToResturn)
            if currentNode.left != None:
                myQuque.append((currentNode.left,index+1))
            if currentNode.right != None:
                myQuque.append((currentNode.right,index+1))
        return lastToResturn

        