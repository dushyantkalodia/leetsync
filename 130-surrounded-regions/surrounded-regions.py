class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(board: List[List[str]],i,j):
            if i<0 or i >= len(board) or j<0 or j>=len(board[0]) or board[i][j] != 'O':
                return 
            board[i][j] = '#'
            dfs(board,i+1,j)
            dfs(board,i-1,j)
            dfs(board,i,j+1)
            dfs(board,i,j-1)
        
        if len(board) == 0:
            return
        for i in range(len(board[0])):
            if board[0][i] == 'O':
                dfs(board,0,i)
            if board[len(board) - 1][i] == 'O':
                dfs(board,len(board)-1,i)
        
        for i in range(len(board)):
            if board[i][0] == 'O':
                dfs(board,i,0)
            if board[i][len(board[0]) - 1] == 'O':
                dfs(board,i,len(board[0])-1)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j] == '#'):
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'