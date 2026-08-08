class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        for i in range(n):
            seen = set()
            for j in range(n):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])
        
        for k in range(n):
            seen = set()
            for m in range(n):
                if board[m][k] == ".":
                    continue
                if board[m][k] in seen:
                    return False
                seen.add(board[m][k])

        move = [[0,0],[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[1,-1],[-1,1],[1,1]]
        l = [1,4,7]
        for i in l:
            for j in l:
                seen = set()
                for k in move:
                    if board[(i+k[0])][(j+k[1])] == ".":
                        continue
                    if board[(i+k[0])][(j+k[1])] in seen:
                        return False
                    seen.add(board[(i+k[0])][(j+k[1])])
    
        return True



        