class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        leftToRightArray = [] # need x axis vvalue
        bottomToTopArray = [] # need y axis value
        for i in range(len(rectangles)):
            x1, y1, x2, y2 = rectangles[i][0],rectangles[i][1],rectangles[i][2],rectangles[i][3]
            leftToRightArray.append([x1,x2])
            bottomToTopArray.append([y1,y2])
        a = self.minInterval(leftToRightArray)
        b = self.minInterval(bottomToTopArray)
        return a or b
    
    def minInterval(self,array):
        array.sort(key=lambda x: x[0])
        count = 0
        prev = [0,0]
        for i in range(len(array)):
            if prev[1] <= array[i][0]:
                count += 1
            prev[1] = max(prev[1],array[i][1])
        return count >= 3