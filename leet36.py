class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows={}
        columns={}
        cells={}
        for row in xrange(9):
            for column in xrange(9):
                if row ==0:
                    columns[column]=[]
                    cells[column]=[]
                    rows[column]=[]
                cur = board[row][column]
                if cur != '.':
                    if (cur in rows[row]) or (cur in columns[column]) or (cur in cells[row/3*3+column/3]):
                        return False
                    rows[row].append(cur)
                    columns[column].append(cur)
                    cells[row/3*3+column/3].append(cur)
        return True
        
