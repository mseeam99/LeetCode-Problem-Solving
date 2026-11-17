class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        for i in range(len(board)):
            rowSet = set()
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in rowSet:
                    rowSet.add(board[i][j])
                else:
                    return False
        
        for i in range(len(board[0])):
            colSet = set()
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                if board[j][i] not in colSet:
                    colSet.add(board[j][i])
                else:
                    return False

        def functionIterate3by3Board(row,col):
            visitedElement = set()
            for r in range(3):
                for c in range(3):
                    rowIdx = row+r
                    colIdx = col+c
                    if board[rowIdx][colIdx] == ".":
                        continue
                    element = int(board[rowIdx][colIdx])
                    if element not in visitedElement and element >= 1 and element <= 9:
                        visitedElement.add(element)
                    else:
                        return False
            return True


        array = [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]

        for i in range(len(array)):
            r,c = array[i][0],array[i][1]
            if functionIterate3by3Board(r,c) == False:
                return False
        
        return True

