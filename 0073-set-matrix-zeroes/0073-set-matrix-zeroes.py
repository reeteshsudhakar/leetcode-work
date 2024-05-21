class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        coords_cleared = set()
        
        def clear_row(i: int):
            for j in range(len(matrix[i])):
                if matrix[i][j] != 0:
                    coords_cleared.add((i, j))
                    matrix[i][j] = 0
                
        
        def clear_col(j: int):
            for i in range(len(matrix)):
                if matrix[i][j] != 0:
                    coords_cleared.add((i, j))
                    matrix[i][j] = 0
        
        for i in range(len(matrix)):
            if 0 not in matrix[i]: continue
            for j in range(len(matrix[0])):
                val = matrix[i][j]
                if val == 0 and (i, j) not in coords_cleared:
                    clear_row(i)
                    clear_col(j)
        
        