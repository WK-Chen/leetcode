class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        len_m, len_n = len(matrix), len(matrix[0])
        row, col = [False] * len_m, [False] * len_n

        for i in range(len_m):
            for j in range(len_n):
                if not matrix[i][j]:
                    row[i] = True
                    col[j] = True
        
        for i in range(len_m):
            for j in range(len_n):
                if row[i] or col[j]:
                    matrix[i][j] = 0
