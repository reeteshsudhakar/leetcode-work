class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rowMap = collections.defaultdict(set)
        colMap = collections.defaultdict(set)
        gridMap = collections.defaultdict(set)
        
        for row in range(len(board)):
            for column in range(len(board)):
                if (board[row][column] == '.'):
                    continue
                if (board[row][column] in rowMap[row] or
                    board[row][column] in colMap[column] or
                    board[row][column] in gridMap[(row // 3, column // 3)]):
                    return False
                else:
                    rowMap[row].add(board[row][column])
                    colMap[column].add(board[row][column])
                    gridMap[(row // 3, column // 3)].add(board[row][column])
        
        return True
                