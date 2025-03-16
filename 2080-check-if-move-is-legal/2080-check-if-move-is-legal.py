class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:

        board[rMove][cMove] = color
        iterationCount = 0
        tempSet = set()

        def recursion(r,c,color,command):

            nonlocal iterationCount

            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return
        
            if iterationCount > 0:
                if board[r][c] != color and board[r][c] != ".":
                    iterationCount+=1
                elif board[r][c] == ".":
                    tempSet.add(False)
                    return
                elif board[r][c] == color:
                    iterationCount+=1
                    if iterationCount >= 3:
                        tempSet.add(True)
                        return
                    else:
                        tempSet.add(False)
                        return
                    
            if iterationCount <= 0:
                iterationCount+=1

            if command == "right":
                recursion(r,c+1,color,command)
            if command == "down":
                recursion(r+1,c,color,command)
            if command == "left":
                recursion(r,c-1,color,command)
            if command == "up":
                recursion(r-1,c,color,command)
            if command == "up_right":
                recursion(r-1,c+1,color,command)
            if command == "down_right":
                recursion(r+1,c+1,color,command)
            if command == "up_left":
                recursion(r-1,c-1,color,command)
            if command == "down_left":
                recursion(r+1,c-1,color,command)

            if True in tempSet:
                return True
            else:
                return False



        listOfCommand = ["right","down","left","up","up_right","down_right","up_left","down_left"]
        answerSet = set()
        for i in listOfCommand:
            answerSet.add(recursion(rMove,cMove,color,i))
            tempSet.clear()
            iterationCount = 0
        if True in answerSet:
            return True
        else:
            return False

        
    
            
       