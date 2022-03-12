"""
被围绕的区域

给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例 1：
输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。
     任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

示例 2：
输入：board = [["X"]]
输出：[["X"]]

提示：
* m == board.length
* n == board[i].length
* 1 <= m, n <= 200
* board[i][j] 为 'X' 或 'O'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/surrounded-regions
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # 深度优先搜索边缘'O'的连通区域，将未连通的区域设为'X'
        height, width = len(board), len(board[0])
        visitss = [[False] * width for _ in range(height)]

        def dfs(x, y: int):
            if x < 0 or x >= height or y < 0 or y >= width or board[x][y] == 'X' or visitss[x][y]:
                return
            visitss[x][y] = True
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        for i in range(width):
            dfs(0, i)
            dfs(height - 1, i)
        for i in range(1, height - 1):
            dfs(i, 0)
            dfs(i, width - 1)
        for i in range(height):
            for j in range(width):
                if not visitss[i][j]:
                    board[i][j] = 'X'


if __name__ == '__main__':
    s = Solution()

    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    s.solve(board)
    print(board)

    board = [["X"]]
    s.solve(board)
    print(board)
