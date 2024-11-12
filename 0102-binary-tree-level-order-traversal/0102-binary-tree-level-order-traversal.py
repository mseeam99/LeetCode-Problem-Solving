class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = [] 
        indexArray = [0]
        self.recursionAgain(root,indexArray)
        for i in range(indexArray[0]):
            answer.append([])
        self.recursion(root,answer,0)
        finalAnswer = []
        for i in range(len(answer)):
            if len(answer[i]) != 0:
                finalAnswer.append(answer[i])
        return finalAnswer

    def recursion(self,root,answer,index):
        if root == None:
            return
        self.recursion(root.left, answer,index+1)
        self.recursion(root.right,answer,index+1)
        answer[index].append(root.val)

    def recursionAgain(self,root,indexArray):
        if root == None:
            return
        indexArray[0] = indexArray[0] + 1
        self.recursionAgain(root.left, indexArray)
        self.recursionAgain(root.right,indexArray)
        

    

       

        