class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):
            row = []
            for j in range(len(board[i])):
                if board[i][j] in row:
                    return False
                elif board[i][j] not in row and board[i][j] != ".":
                    row.append(board[i][j])
        
        for i in range(len(board)):
            column = []
            for j in range(len(board[i])):
                if board[j][i] in column:
                    return False
                elif board[j][i] not in column and board[j][i] != ".":
                    column.append(board[j][i])

        for row in range(0,9,3):
            for column in range(0,9,3):
                subMatrix = []
                for i in range(row,row+3):
                    for j in range(column,column+3):
                        if board[i][j] in subMatrix:
                            return False
                        elif board[i][j] not in subMatrix and board[i][j] != ".":
                            subMatrix.append(board[i][j])
                            
        return True



            

            





        
        
        

        

        
 



        