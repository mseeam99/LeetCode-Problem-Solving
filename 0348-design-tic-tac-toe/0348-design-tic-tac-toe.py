class TicTacToe:

    def __init__(self, n: int):
        self.array = []
        for i in range(n):
            subArray = [0] * n
            self.array.append(subArray)

    def move(self, row: int, col: int, player: int) -> int:
        sign = None
        if player == 1:
            sign = "X"
        elif player == 2:
            sign = "Y"
        self.array[row][col] = sign
        
        def check_rowWise_Linear(row,col,sign):
            for i in range(len(self.array[row])):
                if self.array[row][i] != sign:
                    return False
            return True

        def check_colWise_Linear(row,col,sign):
            for i in range(len(self.array)):
                if self.array[i][col] != sign:
                    return False
            return True

        def check_DIagonal_leftToRight(row,col,sign):
            for i in range(len(self.array)):
                if self.array[i][i] != sign:
                    return False
            return True

        def check_DIagonal_RightToLeft(row,col,sign):
            n = len(self.array)
            for i in range(n):
                if self.array[i][n - 1 - i] != sign:
                    return False
            return True

        if ((check_rowWise_Linear(row,col,sign) == True)        or 
            (check_colWise_Linear(row,col,sign) == True)        or 
            (check_DIagonal_leftToRight(row,col,sign) == True)  or 
            (check_DIagonal_RightToLeft(row,col,sign) == True)):
            return player
        
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)