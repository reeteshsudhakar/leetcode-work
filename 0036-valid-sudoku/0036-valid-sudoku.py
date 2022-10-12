from collections import defaultdict

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        rowMap = defaultdict(list)
        colMap = defaultdict(list)
        boxMap = defaultdict(list)
        
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in rowMap[i] or board[i][j] in colMap[j] or board[i][j] in boxMap[(i // 3, j // 3)]:
                    return False
                else: 
                    rowMap[i] += board[i][j]
                    colMap[j] += board[i][j]
                    boxMap[(i // 3, j // 3)] += board[i][j]
        
        
                    
        return True
        