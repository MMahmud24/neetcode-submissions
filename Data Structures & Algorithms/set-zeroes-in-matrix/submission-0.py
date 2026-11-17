class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        firstRow = False
        firstCol = False

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            if matrix[i][0] == 0:
                firstCol = True

        for i in range(n):
            if matrix[0][i] == 0:
                firstRow = True

        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            if matrix[i][0] == 0:
                matrix[i] = [0] * n
        
        for i in range(1,n):
            if matrix[0][i] == 0:
                for j in range(m):
                    matrix[j][i] = 0

        if firstRow:
            matrix[0] = [0] * n

        if firstCol:
            for i in range(m):
                matrix[i][0] = 0


        