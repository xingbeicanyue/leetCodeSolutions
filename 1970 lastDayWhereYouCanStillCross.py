"""
你能穿过矩阵的最后一天

给你一个下标从 1 开始的二进制矩阵，其中 0 表示陆地，1 表示水域。同时给你 row 和 col 分别表示矩阵中行和列的数目。

一开始在第 0 天，整个矩阵都是陆地。但每一天都会有一块新陆地被水淹没变成水域。给你一个下标从 1 开始的二维数组 cells ，
其中 cells[i] = [ri, ci] 表示在第 i 天，第 ri 行 ci 列（下标都是从 1 开始）的陆地会变成水域（也就是 0 变成 1 ）。

你想知道从矩阵最上面一行走到最下面一行，且只经过陆地格子的最后一天是哪一天。
你可以从最上面一行的任意格子出发，到达最下面一行的任意格子。
你只能沿着四个基本方向移动（也就是上下左右）。

请返回只经过陆地格子能从最上面一行走到最下面一行的最后一天。

示例 1：
  0 0  ->  1 0  ->  1 0  ->  1 1
  0 0      0 0      1 0      1 0
输入：row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
输出：2
解释：上图描述了矩阵从第 0 天开始是如何变化的。
可以从最上面一行到最下面一行的最后一天是第 2 天。

示例 2：
  0 0  ->  1 0  ->  1 1
  0 0      0 0      0 0
输入：row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]
输出：1
解释：上图描述了矩阵从第 0 天开始是如何变化的。
可以从最上面一行到最下面一行的最后一天是第 1 天。

示例 3：
  0 0 0      0 1 0      0 1 0      0 1 0      0 1 0
  0 0 0  ->  0 0 0  ->  1 0 0  ->  1 0 0  ->  1 1 0
  0 0 0      0 0 0      0 0 0      0 0 1      0 0 1
输入：row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
输出：3
解释：上图描述了矩阵从第 0 天开始是如何变化的。
可以从最上面一行到最下面一行的最后一天是第 3 天。

提示：
* 2 <= row, col <= 2 * 10^4
* 4 <= row * col <= 2 * 10^4
* cells.length == row * col
* 1 <= ri <= row
* 1 <= ci <= col
* cells 中的所有格子坐标都是唯一的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/last-day-where-you-can-still-cross
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：深度优先搜索、广度优先搜索、并查集、数组、二分查找、矩阵
"""

from typing import List


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        # 反向思考：将全是水的区域逐个填上陆地，求连通第一行和最后一行的天数（反向思考为4连通，正向思考为8连通）
        # 使用并查集，对于每块陆地，如果上下左右也是陆地则与其连接，连接后判断该群组是否连通第一行和最后一行

        def findRoot(disjointSet: List[List[List[int]]], y, x) -> List[int]:
            """ 查找并查集根节点 """
            parentNode = disjointSet[y][x]
            nodes = []
            while parentNode[0] != y or parentNode[1] != x:
                nodes.append((y, x))
                y, x = parentNode[0], parentNode[1]
                parentNode = disjointSet[y][x]
            for node in nodes:  # 压缩路径
                disjointSet[node[0]][node[1]] = parentNode
            return parentNode

        def union(disjointSet: List[List[List[int]]], y1, x1, y2, x2):
            """ 合并，返回合并后的群组是否连通第一行和最后一行 """
            r1, r2 = findRoot(disjointSet, y1, x1), findRoot(disjointSet, y2, x2)
            if r1 is not r2:
                r1[2], r1[3] = min(r1[2], r2[2]), max(r1[3], r2[3])
                disjointSet[r2[0]][r2[1]] = r1
            return r1[2] <= 1 and r1[3] >= row

        # 并查集：[[父节点行号, 列号, 群组最小行号, 群组最大行号, 是否陆地]]
        disjointSet = [[[y, x, y, y, False] for x in range(col + 2)] for y in range(row + 2)]
        for i, cell in enumerate(reversed(cells)):
            y, x = cell[0], cell[1]
            disjointSet[y][x][4] = True
            if (disjointSet[y - 1][x][4] and union(disjointSet, y, x, y - 1, x)) or\
               (disjointSet[y + 1][x][4] and union(disjointSet, y, x, y + 1, x)) or\
               (disjointSet[y][x - 1][4] and union(disjointSet, y, x, y, x - 1)) or\
               (disjointSet[y][x + 1][4] and union(disjointSet, y, x, y, x + 1)):
                return len(cells) - i - 1
        return 0


if __name__ == '__main__':
    s = Solution()

    r = s.latestDayToCross(2, 2, [[1, 1], [2, 1], [1, 2], [2, 2]])
    print(r)

    r = s.latestDayToCross(2, 2, [[1, 1], [1, 2], [2, 1], [2, 2]])
    print(r)

    r = s.latestDayToCross(3, 3, [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]])
    print(r)
