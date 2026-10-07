class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        sub_grids = defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell == ".":
                    continue
                else:
                    if cell in rows[i]:
                        return False

                    rows[i].add(cell)
                    
                    if cell in columns[j]:
                        return False
                    
                    columns[j].add(cell)

                    if cell in sub_grids[(i//3, j//3)]:
                        return False
                    sub_grids[(i//3, j//3)].add(cell)
                

        return True