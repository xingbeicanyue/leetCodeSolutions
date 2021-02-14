"""
岛屿数量

给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。

示例 1：
输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1

示例 2：
输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3

提示：
* m == grid.length
* n == grid[i].length
* 1 <= m, n <= 300
* grid[i][j] 的值为 '0' 或 '1'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：深度优先搜索、广度优先搜索、并查集
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        grid = [row[:] for row in grid]  # 为了不修改原数据而克隆
        result = 0
        for x, row in enumerate(grid):
            for y, ele in enumerate(row):
                if ele == '1':
                    self._fill(grid, x, y)
                    result += 1
        return result

    def _fill(self, grid: List[List[str]], x: int, y: int):
        """ 填充与grid[x][y]连通的区域（扫描线种子填充算法） """

        def fillEle(x: int, y: int):
            grid[x][y] = '0'
            fillings.append((x - 1, y))
            fillings.append((x + 1, y))

        def fillRow(x: int, y: int):
            if x < 0 or x >= gridLen or grid[x][y] == '0':
                return
            fillEle(x, y)
            for i in range(y + 1, rowLen):
                if grid[x][i] == '0':
                    break
                fillEle(x, i)
            for i in range(y - 1, -1, -1):
                if grid[x][i] == '0':
                    break
                fillEle(x, i)

        gridLen, rowLen = len(grid), len(grid[0])
        fillings = [(x, y)]  # [待填充的坐标]
        while len(fillings) > 0:
            fillRow(*fillings.pop())


if __name__ == '__main__':
    s = Solution()
    r = s.numIslands([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ])
    print(r)
    r = s.numIslands([
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ])
    print(r)
