class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        def generate_empty_grid(dim: int) -> List[List[int]]:
            return [[0 for i in range(dim - 2)] for j in range(dim - 2)]
        
        def compute_max_val(i: int, j: int) -> int:
            row, col = i + 1, j + 1
            max_val = None
            for x in range(row - 1, row + 2):
                for y in range(col - 1, col + 2):
                    print(grid[x][y])
                    if max_val is None or grid[x][y] > max_val: 
                        max_val = grid[x][y]
            
            return max_val
                    
        
        ret = generate_empty_grid(dim=len(grid[0]))
        
        for i in range(len(ret)):
            for j in range(len(ret[0])):
                ret[i][j] = compute_max_val(i, j)
        
        return ret