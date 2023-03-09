from collections import deque
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        queue = deque()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    print(1)
                    ans = self.sol(i, j, word[0], board, word)
                    if ans == True:
                        return True
        return False

    def sol(self, i: int, j: int, c: str,  board: List[List[str]], word: str):
        queue = deque()
        queue.append((i, j, c))
        x, y = [0, 0, 1, -1], [1, -1, 0, 0]
        while queue:
            i, j, c = queue.popleft()
            print(c)
            if c == word:
                return True
            for dir in range(4):
                ii, jj = i + x[dir], j + y[dir]
                if ii < 0 or jj < 0 or ii >= len(board) or jj >= len(board[0]):
                    continue
                if len(word) > len(c):
                    if board[ii][jj] != word[len(c)]:
                        continue
                queue.append((ii, jj, c + board[ii][jj]))
        return


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
sol = Solution()
ans = sol.exist(board=board, word=word)
print(ans)
