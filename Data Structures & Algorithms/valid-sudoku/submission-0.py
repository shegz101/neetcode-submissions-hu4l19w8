class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_set = [set() for _ in range(9)]
        cols_set = [set() for _ in range(9)]
        threebythree_set = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                box_id = (r // 3) * 3 + (c // 3)
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows_set[r] or board[r][c] in cols_set[c] or board[r][c] in threebythree_set[box_id]:
                    return False
                rows_set[r].add(board[r][c])
                cols_set[c].add(board[r][c])
                threebythree_set[box_id].add(board[r][c])
        
        return True 