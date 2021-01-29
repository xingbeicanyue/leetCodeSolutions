"""
最小体力消耗路径

你准备参加一场远足活动。给你一个二维 rows x columns 的地图 heights ，其中 heights[row][col] 表示格子 (row, col) 的高度。
一开始你在最左上角的格子 (0, 0) ，且你希望去最右下角的格子 (rows-1, columns-1) （注意下标从 0 开始编号）。
你每次可以往上，下，左，右四个方向之一移动，你想要找到耗费体力最小的一条路径。
一条路径耗费的体力值是路径上相邻格子之间高度差绝对值的最大值决定的。
请你返回从左上角走到右下角的最小体力消耗值。

示例 1：
    1    2    2
    |
    3    8    2
    |
    5----3----5
输入：heights = [[1,2,2],[3,8,2],[5,3,5]]
输出：2
解释：路径 [1,3,5,3,5] 连续格子的差值绝对值最大为 2 。
这条路径比路径 [1,2,2,2,5] 更优，因为另一条路径差值最大值为 3 。

示例 2：
    1----2----3
              |
    3    8    4
              |
    5    3    5
输入：heights = [[1,2,3],[3,8,4],[5,3,5]]
输出：1
解释：路径 [1,2,3,4,5] 的相邻格子差值绝对值最大为 1 ，比路径 [1,3,5,3,5] 更优。

示例 3：
    1    2    1----1----1
    |         |         |
    1    2    1    2    1
    |         |         |
    1    2    1    2    1
    |         |         |
    1    2    1    2    1
    |         |         |
    1----1----1    2    1
输入：heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
输出：0
解释：上图所示路径不需要消耗任何体力。

提示：
* rows == heights.length
* columns == heights[i].length
* 1 <= rows, columns <= 100
* 1 <= heights[i][j] <= 10^6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-with-minimum-effort
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：深度优先搜索、并查集、图、二分查找
"""

from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])
        if n == m == 1:
            return 0
        edges = []
        for i in range(n):
            for j in range(m):
                curIdx = i * m + j
                if j < m - 1:
                    edges.append([abs(heights[i][j] - heights[i][j + 1]), curIdx, curIdx + 1])
                if i < n - 1:
                    edges.append([abs(heights[i][j] - heights[i + 1][j]), curIdx, curIdx + m])
        edges.sort()
        disjointSet, lastRoot = [-1] * (n * m), n * m - 1  # 并查集 | 最后一个节点的根节点
        for edge in edges:
            r1, r2 = self._getRoot(disjointSet, edge[1]), self._getRoot(disjointSet, edge[2])
            if r1 != r2:
                minR, maxR = min(r1, r2), max(r1, r2)
                disjointSet[maxR] = minR  # 保证下标更小的为根节点
                if maxR == lastRoot:
                    if minR == 0:
                        return edge[0]
                    lastRoot = minR

    def _getRoot(self, disjointSet: List[int], idx: int):
        """ 获取idx在并查集的根节点 """
        visiteds = []
        while disjointSet[idx] >= 0:
            visiteds.append(idx)
            idx = disjointSet[idx]
        for visited in visiteds:
            disjointSet[visited] = idx
        return idx


if __name__ == '__main__':
    s = Solution()
    r = s.minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]])
    print(r)
    r = s.minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]])
    print(r)
    r = s.minimumEffortPath([[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]])
    print(r)
