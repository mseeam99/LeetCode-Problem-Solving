class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        hashMap = {}
        for i in range(len(matrix)):
            row = matrix[i]
            if row[0] != 0:
                for j in range(len(row)):
                    row[j] = row[j] ^ 1
            if tuple(row) in hashMap:
                hashMap[tuple(row)] += 1
            else:
                hashMap[tuple(row)] = 1
        return max(hashMap.values())