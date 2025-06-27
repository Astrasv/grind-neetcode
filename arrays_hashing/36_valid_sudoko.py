from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        def check_row(board):
            for i in range(rows):
                visited = set()
                for j in range(cols):
                    if board[i][j] in visited and board[i][j] != ".":
                        return False
                    visited.add(board[i][j])
            
            return True
        
        def check_col(board):
            for i in range(cols):
                visited = set()
                for j in range(rows):
                    if board[j][i] in visited and board[j][i] != ".":
                        return False
                    visited.add(board[j][i])
            return True
            
        def check_box(board):
            for row_ptr in range(0,rows,3):
                for col_ptr in range(0,cols,3):
                    visited = set()
                    for i in range(row_ptr,row_ptr+3):
                        for j in range(col_ptr,col_ptr+3):
                            if board[i][j] in visited and board[i][j] != ".":
                                return False
                            visited.add(board[i][j])
            return True

        return check_row(board) and check_col(board) and check_box(board)
        
        