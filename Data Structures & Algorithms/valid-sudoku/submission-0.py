class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        for i in range(n):
            seen1 = set()
            for j in range(n):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen1:
                    return False
                seen1.add(board[i][j])
        
        for k in range(n):
            seen2 = set()
            for m in range(n):
                if board[m][k] == ".":
                    continue
                if board[m][k] in seen2:
                    return False
                seen2.add(board[m][k])

        move = [[0,0],[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[1,-1],[-1,1],[1,1]]
        l = [1,4,7]
        for i in l:
            for j in l:
                seen3 = set()
                for k in move:
                    if board[(i+k[0])][(j+k[1])] == ".":
                        continue
                    if board[(i+k[0])][(j+k[1])] in seen3:
                        return False
                    seen3.add(board[(i+k[0])][(j+k[1])])
    
        return True



        