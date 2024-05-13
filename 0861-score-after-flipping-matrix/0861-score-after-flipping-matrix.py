class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:        
        
        def flipRow(grid: List[List[int]], row: int):
            for i in range(len(grid[row])):
                grid[row][i] = 0 if grid[row][i] == 1 else 1 
        
        def flipCol(grid: List[List[int]], col: int):
            for i in range(len(grid)):
                grid[i][col] = 0 if grid[i][col] == 1 else 1
        
        for i in range(len(grid)):
            if grid[i][0] == 0: 
                flipRow(grid, i)
                
        for j in range(len(grid[0])):
            num_zeroes = 0 
            for i in range(len(grid)):
                if grid[i][j] == 0: num_zeroes += 1
            
            if num_zeroes > len(grid) // 2: flipCol(grid, j)
        
                
        def compute_solution(grid): 
            result = 0 
            for arr in grid:
                num = int(''.join([str(item) for item in arr]), 2)
                result += num
            return result 
        
        return compute_solution(grid)