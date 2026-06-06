from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        blocks = defaultdict(set)

        for row in range(9):
            for col in range(9):
                currElem = board[row][col]
                if currElem == '.':
                    continue
                if (currElem in rows[row] or currElem in cols[col] or
                    currElem in blocks[(row // 3, col // 3)]):
                    return False
                rows[row].add(currElem)
                cols[col].add(currElem)
                blocks[(row // 3, col //3)].add(currElem)
        return True
        