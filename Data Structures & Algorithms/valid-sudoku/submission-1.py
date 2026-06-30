class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        subb = defaultdict(set)

        for i in range(9):
            for j in range(9):

                if board[i][j] == '.':
                    continue
                
                if board[i][j] in rows[i] or board[i][j] in cols[i] or board[i][j] in subb[(i//3,j//3)]:
                    return False
                
                rows[r].add(board[i][j])
                cols[c].add(board[i][j])
                subb[(r//3,c//3)].add(board[i][j])

        return True