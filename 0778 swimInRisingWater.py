"""
水位上升的泳池中游泳

在一个 N x N 的坐标方格 grid 中，每一个方格的值 grid[i][j] 表示在位置 (i,j) 的平台高度。
现在开始下雨了。当时间为 t 时，此时雨水导致水池中任意位置的水位为 t 。
你可以从一个平台游向四周相邻的任意一个平台，但是前提是此时水位必须同时淹没这两个平台。
假定你可以瞬间移动无限距离，也就是默认在方格内部游动是不耗时的。当然，在你游泳的时候你必须待在坐标方格里面。
你从坐标方格的左上平台 (0，0) 出发。最少耗时多久你才能到达坐标方格的右下平台 (N-1, N-1)？

示例 1:
输入: [[0,2],[1,3]]
输出: 3
解释:
时间为0时，你位于坐标方格的位置为 (0, 0)。
此时你不能游向任意方向，因为四个相邻方向平台的高度都大于当前时间为 0 时的水位。
等时间到达 3 时，你才可以游向平台 (1, 1). 因为此时的水位是 3，坐标方格中的平台没有比水位 3 更高的，
所以你可以游向坐标方格中的任意位置

示例2:
输入: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
输出: 16
解释:
 0 -- 1 -- 2 -- 3 -- 4
                     |
24   23   22   21    5
                     |
12 - 13 - 14 - 15 - 16
 |
11   17   18   19   20
 |
10 -- 9 -- 8 -- 7 -- 6
我们必须等到时间为 16，此时才能保证平台 (0, 0) 和 (4, 4) 是连通的

提示:
* 2 <= N <= 50.
* grid[i][j] 是 [0, ..., N*N - 1] 的排列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swim-in-rising-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        disjointSet = [-1] * (n * n)  # 并查集，-1表示未访问
        lastRoot = n * n - 1
        for g in sorted([g, i, j] for i, row in enumerate(grid) for j, g in enumerate(row)):
            idx = g[1] * n + g[2]
            disjointSet[idx] = idx
            if g[1] >= 1:
                lastRoot = self._merge(disjointSet, idx, idx - n, lastRoot)
            if g[1] <= n - 2:
                lastRoot = self._merge(disjointSet, idx, idx + n, lastRoot)
            if g[2] >= 1:
                lastRoot = self._merge(disjointSet, idx, idx - 1, lastRoot)
            if g[2] <= n - 2:
                lastRoot = self._merge(disjointSet, idx, idx + 1, lastRoot)
            if lastRoot == 0:  # 形成通路
                return g[0]

    def _merge(self, disjointSet: List[int], idx1: int, idx2: int, lastRoot: int) -> int:
        """ 合并并查集中的两个元素
        :returns: 最后一个元素的根节点
        """
        if disjointSet[idx2] < 0:
            return lastRoot
        r1 = self._getRoot(disjointSet, idx1)
        r2 = self._getRoot(disjointSet, idx2)
        minR, maxR = min(r1, r2), max(r1, r2)
        disjointSet[maxR] = minR
        return minR if maxR == lastRoot else lastRoot

    def _getRoot(self, disjointSet: List[int], idx: int) -> int:
        """ 获取并查集中的根节点 """
        visiteds = []
        while idx != disjointSet[idx]:
            visiteds.append(idx)
            idx = disjointSet[idx]
        for visited in visiteds:
            disjointSet[visited] = idx
        return idx


if __name__ == '__main__':
    s = Solution()
    r = s.swimInWater([[0, 2], [1, 3]])
    print(r)
    r = s.swimInWater(
        [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]])
    print(r)
