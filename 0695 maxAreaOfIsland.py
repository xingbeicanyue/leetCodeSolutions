"""
岛屿的最大面积

给你一个大小为 m x n 的二进制矩阵 grid 。

岛屿是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直的四个方向上相邻。
你可以假设 grid 的四个边缘都被 0（代表水）包围着。

岛屿的面积是岛上值为 1 的单元格的数目。
计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。

示例 1：
输入：grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
             [0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,1,1,0,1,0,0,0,0,0,0,0,0],
             [0,1,0,0,1,1,0,0,1,0,1,0,0],
             [0,1,0,0,1,1,0,0,1,1,1,0,0],
             [0,0,0,0,0,0,0,0,0,0,1,0,0],
             [0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,0,0,0,0,0,0,1,1,0,0,0,0]]
输出：6
解释：答案不应该是 11 ，因为岛屿只能包含水平或垂直这四个方向上的 1 。

示例 2：
输入：grid = [[0,0,0,0,0,0,0,0]]
输出：0

提示：
* m == grid.length
* n == grid[i].length
* 1 <= m, n <= 50
* grid[i][j] 为 0 或 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-area-of-island
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 深度优先遍历，记录访问过的位置防止重复访问
        height, width = len(grid), len(grid[0])
        visitss = [[False] * width for _ in range(height)]  # 记录每个格子是否访问过

        def dfs(i, j: int) -> int:
            """ 深度优先遍历grid[i][j]
            :return: 返回遍历格数
            """
            if i < 0 or i >= height or j < 0 or j >= width or grid[i][j] == 0 or visitss[i][j]:
                return 0
            visitss[i][j] = True
            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)

        return max(dfs(i, j) for i in range(height) for j in range(width))


if __name__ == '__main__':
    s = Solution()

    r = s.maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                           [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                           [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]])
    print(r)

    r = s.maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]])
    print(r)
