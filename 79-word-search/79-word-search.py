from collections import Counter
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        ROWS, COLS = len(board), len(board[0])
        
        word_dict = Counter(word)
        board_dict = Counter(chain.from_iterable(board))
        
        if any(count > board_dict[char] for char, count in word_dict.items()):
            return False
        
        if word_dict[word[0]] > word_dict[word[len(word) - 1]]:
            word = word[::-1]
            
        def dfs(r, c, k):
            if k == len(word) - 1:
                return True
            
            moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for x, y in moves:
                i = x + r
                j = y + c
                if (0 <= i < ROWS and 0 <= j < COLS and board[i][j] == word[k + 1]):
                    temp = board[i][j]
                    board[i][j] = "."
                    if dfs(i, j, k + 1):
                        return True
                    board[i][j] = temp
            return False
 
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    temp = board[i][j]
                    board[i][j] = "."
                    
                    if dfs(i, j, 0):
                        return True
                    board[i][j] = temp
        return False
        