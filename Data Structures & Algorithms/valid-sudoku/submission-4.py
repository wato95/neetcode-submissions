class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = {i:set() for i in range(9)}
        cols = {i:set() for i in range(9)}
        boxes = {i:set() for i in range(9)}

        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num == '.':
                    continue
                
                box = ((i//3) * 3) + ((j//3))
                if (num in rows[i]) or (num in cols[j]) or (num in boxes[box]):
                    return False
                else:
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box].add(num)
        
        return True



