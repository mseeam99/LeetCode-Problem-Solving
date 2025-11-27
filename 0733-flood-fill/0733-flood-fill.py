class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        seen = set()
        fixedColor = image[sr][sc]
        def recursion(row,col):
            if (row,col) in seen or row < 0 or row >= len(image) or col < 0 or col >= len(image[0]) or image[row][col] != fixedColor:
                return
            image[row][col] = color
            seen.add((row,col))
            recursion(row,col+1)
            recursion(row+1,col)
            recursion(row,col-1)
            recursion(row-1,col)
        recursion(sr,sc)
        return image






        