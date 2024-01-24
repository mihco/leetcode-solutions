class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check rows
        for i in range(len(board)):
            num_cts = [0] * 9
            for j in range(len(board)):
                if(board[i][j] != "."):
                    num_cts[int(board[i][j]) - 1] += 1
                    if(num_cts[int(board[i][j]) - 1] > 1):
                        return False           
        
        # check columns
        for i in range(len(board)):
            num_cts = [0] * 9
            for j in range(len(board)):
                if(board[j][i] != "."):
                    num_cts[int(board[j][i]) - 1] += 1
                    if(num_cts[int(board[j][i]) - 1] > 1):
                        return False
                    
        # check boxes
        boxes = {}
        for i in range(len(board)//3):
            for j in range(len(board)//3):
                boxes[(i, j)] = [0] * 9
        for i in range(len(board)):
            for j in range(len(board)):
                if(board[i][j] != "."):
                        boxes[(i//3,j//3)][int(board[i][j]) - 1] += 1
                        if(boxes[(i//3,j//3)][int(board[i][j]) - 1] > 1):
                            return False     
            
        
        return True