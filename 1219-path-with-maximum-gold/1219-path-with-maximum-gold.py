class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ret = 0
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def search(i: int, j: int):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            
            max_val = 0
            curr_val = grid[i][j]
            grid[i][j] = 0
            
            for x, y in DIRECTIONS:
                max_val = max(max_val, search(i + x, j + y))
                
            grid[i][j] = curr_val
            return max_val + curr_val
            
            
            
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ret = max(ret, search(i, j))
        
        return ret