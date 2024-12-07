# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        index=[0]
        self.getHeightByDFS(root,index,0)
        height = index[0]-1
        M = index[0]
        N = (2**(height+1))-1
        result = []
        for i in range(M):
            tempList = []
            for j in range(N):
                tempList.append("")
            result.append(tempList)
        r,c = 0,(N-1)//2
        self.functionBFS(root,result,r,c,height)
        return result

    def functionBFS(self,root,result,r,c,height):
        if root == None:
            return
        myQueue = deque([(root,r,c)] if root else [])
        while len(myQueue) != 0:
            currentNode, r, c = myQueue.popleft()
            result[r][c] = str(currentNode.val)
            if currentNode.left:
                myQueue.append((currentNode.left, r + 1, c - 2**(height - r - 1)))
            if currentNode.right:
                myQueue.append((currentNode.right, r + 1, c + 2**(height - r - 1)))

    def getHeightByDFS(self,root,index,i):
        if root == None:
            return
        i += 1
        index[0] = max(index[0],i)
        self.getHeightByDFS(root.left,index,i)
        self.getHeightByDFS(root.right,index,i)