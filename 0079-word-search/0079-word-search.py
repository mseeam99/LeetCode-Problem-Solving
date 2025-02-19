class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        finalAnswer = [False]

        def backTracking(r, c, index, makingTheString):
            # If finalAnswer[0] is True, no need to proceed further.
            if finalAnswer[0]:
                return
            
            # If out of bounds or the characters do not match:
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != word[index]:
                return
            
            # Update the string with the current character
            makingTheString += board[r][c]

            # Check if we have constructed the word
            if makingTheString == word:
                finalAnswer[0] = True
                return
            
            # Mark this cell as visited by replacing it with a non-letter character
            temp = board[r][c]
            board[r][c] = '#'

            # Move to the next character in the word
            if index + 1 < len(word):
                backTracking(r + 1, c, index + 1, makingTheString)
                backTracking(r - 1, c, index + 1, makingTheString)
                backTracking(r, c + 1, index + 1, makingTheString)
                backTracking(r, c - 1, index + 1, makingTheString)

            # Undo the visit
            board[r][c] = temp

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:  # Start search from cells that contain the first letter of the word
                    backTracking(i, j, 0, "")
                    if finalAnswer[0]:
                        return True

        return finalAnswer[0]

