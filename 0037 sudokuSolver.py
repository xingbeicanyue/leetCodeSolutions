"""
解数独

编写一个程序，通过填充空格来解决数独问题。
数独的解法需 遵循如下规则：
1. 数字 1-9 在每一行只能出现一次。
2. 数字 1-9 在每一列只能出现一次。
3. 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
数独部分空格内已填入了数字，空白格用 '.' 表示。

示例：
输入：board = [["5","3",".",".","7",".",".",".","."],
              ["6",".",".","1","9","5",".",".","."],
              [".","9","8",".",".",".",".","6","."],
              ["8",".",".",".","6",".",".",".","3"],
              ["4",".",".","8",".","3",".",".","1"],
              ["7",".",".",".","2",".",".",".","6"],
              [".","6",".",".",".",".","2","8","."],
              [".",".",".","4","1","9",".",".","5"],
              [".",".",".",".","8",".",".","7","9"]]
输出：[["5","3","4","6","7","8","9","1","2"],
      ["6","7","2","1","9","5","3","4","8"],
      ["1","9","8","3","4","2","5","6","7"],
      ["8","5","9","7","6","1","4","2","3"],
      ["4","2","6","8","5","3","7","9","1"],
      ["7","1","3","9","2","4","8","5","6"],
      ["9","6","1","5","3","7","2","8","4"],
      ["2","8","7","4","1","9","6","3","5"],
      ["3","4","5","2","8","6","1","7","9"]]

提示：
* board.length == 9
* board[i].length == 9
* board[i][j] 是一位数字或者 '.'
* 题目数据 保证 输入数独仅有一个解

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sudoku-solver
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数组、回溯、矩阵
"""

from itertools import product
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # 将字符串替换成数字以提升速度
        # 回溯法：依次对每个位置计算可以填入的数字，然后尝试填入这些数字
        numBoard = [[0 if board[i][j] == '.' else int(board[i][j]) for j in range(9)] for i in range(9)]

        def tryOneEle(i: int, j: int) -> True:
            """ 尝试填入一个位置 """
            if i == 9:
                return True
            # 计算下一个要填入的位置
            if j == 8:
                nextI, nextJ = i + 1, 0
            else:
                nextI, nextJ = i, j + 1

            oriNum = numBoard[i][j]
            if oriNum == 0:
                # 计算可以填入的数字
                candidates = [True] * 10
                for k in range(9):
                    candidates[numBoard[i][k]] = False
                    candidates[numBoard[k][j]] = False
                x, y = i // 3, j // 3
                for m, n in product(range(3 * x, 3 * (x + 1)), range(3 * y, 3 * (y + 1))):
                    candidates[numBoard[m][n]] = False
                # 尝试填入
                for num in range(1, 10):
                    if not candidates[num]:
                        continue
                    numBoard[i][j] = num
                    if tryOneEle(nextI, nextJ):
                        return True
                    numBoard[i][j] = oriNum
            else:
                if tryOneEle(nextI, nextJ):
                    return True

        tryOneEle(0, 0)
        for i in range(9):
            for j in range(9):
                board[i][j] = str(numBoard[i][j])


if __name__ == '__main__':
    s = Solution()

    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    s.solveSudoku(board)
    print(board)
