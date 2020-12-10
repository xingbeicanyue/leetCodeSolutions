"""
在二维网格 grid 上，有 4 种类型的方格：
1 表示起始方格。且只有一个起始方格。
2 表示结束方格，且只有一个结束方格。
0 表示我们可以走过的空方格。
-1 表示我们无法跨越的障碍。
返回在四个方向（上、下、左、右）上行走时，从起始方格到结束方格的不同路径的数目。
每一个无障碍方格都要通过一次，但是一条路径中不能重复通过同一个方格。

示例 1：
输入：[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
输出：2
解释：我们有以下两条路径：
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

示例 2：
输入：[[1,0,0,0],[0,0,0,0],[0,0,0,2]]
输出：4
解释：我们有以下四条路径：
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

示例 3：
输入：[[0,1],[2,0]]
输出：0
解释：
没有一条路能完全穿过每一个空的方格一次。
请注意，起始和结束方格可以位于网格中的任意位置。
 
提示：
* 1 <= grid.length * grid[0].length <= 20

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：深度优先搜索，回溯算法
"""


class Solution:
    def uniquePathsIII(self, grid: list) -> int:

        def visit(rowIdx: int, colIdx: int, toVisitCount: int) -> int:
            """ 访问一个方格
            :param rowIdx: 当前访问的行下标
            :param colIdx: 当前访问的列下标
            :param toVisitCount: 剩余待访问的方格数（包括当前方格）
            :returns: 返回从此开始成功到达终点的次数
            """
            if visitss[rowIdx][colIdx] < 0:
                return 0
            if visitss[rowIdx][colIdx] == 2:
                return 1 if toVisitCount == 1 else 0

            visitss[rowIdx][colIdx] = -1
            result = 0
            toVisitCount -= 1
            # 按上左下右的顺序访问
            if rowIdx >= 1:
                result += visit(rowIdx - 1, colIdx, toVisitCount)
            if colIdx >= 1:
                result += visit(rowIdx, colIdx - 1, toVisitCount)
            if rowIdx <= len(grid) - 2:
                result += visit(rowIdx + 1, colIdx, toVisitCount)
            if colIdx <= len(grid[0]) - 2:
                result += visit(rowIdx, colIdx + 1, toVisitCount)
            visitss[rowIdx][colIdx] = 0
            return result

        visitss = [row[:] for row in grid]  # 已访问表 -1:已访问或障碍 0:未访问
        initRowIdx, initColIdx = -1, -1
        for i, row in enumerate(grid):
            for j, ele in enumerate(row):
                if ele == 1:
                    initRowIdx, initColIdx = i, j
                    break
            if initRowIdx >= 0:
                break
        return visit(initRowIdx, initColIdx, len(grid) * len(grid[0]) - sum(row.count(-1) for row in grid))


if __name__ == '__main__':
    s = Solution()
    r = s.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]])
    print(r)
    r = s.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]])
    print(r)
    r = s.uniquePathsIII([[0, 1], [2, 0]])
    print(r)
