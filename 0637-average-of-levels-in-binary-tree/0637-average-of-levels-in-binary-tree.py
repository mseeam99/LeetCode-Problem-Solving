# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        finalAnswer = []
        myQueue = deque([root] if root else [])
        while len(myQueue) != 0:
            currentSum = 0
            index = 0
            for _ in range(len(myQueue)):
                currentNode = myQueue.popleft()
                currentSum += currentNode.val
                index += 1
                if currentNode.left != None:
                    myQueue.append(currentNode.left)
                if currentNode.right != None:
                    myQueue.append(currentNode.right)
            finalAnswer.append(currentSum/index)
        return finalAnswer
        
