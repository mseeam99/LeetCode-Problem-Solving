# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        answer = []
        index = 1
        bigArray = []
        self.breadthFirstSearch(root,answer,index,bigArray)
        returnArray = []
        groups = {}
        for i in range(len(bigArray)):
            if bigArray[i][1] not in groups:
                groups[bigArray[i][1]] = []  
            groups[bigArray[i][1]].append(bigArray[i][0])
        for key,val in groups.items():
            returnArray.append(max(val))
        return returnArray

    def breadthFirstSearch(self,root,answer,index,bigArray):
        myQueue = deque([(root,index)] if root else None)
        while len(myQueue) != 0:
            currentNode,index = myQueue.popleft()
            bigArray.append([currentNode.val,index])
            if currentNode.left != None:
                myQueue.append((currentNode.left,index+1))
            if currentNode.right != None:
                myQueue.append((currentNode.right,index+1))


        