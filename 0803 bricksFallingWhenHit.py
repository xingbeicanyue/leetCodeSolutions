"""
打砖块

有一个 m x n 的二元网格，其中 1 表示砖块，0 表示空白。砖块稳定（不会掉落）的前提是：
* 一块砖直接连接到网格的顶部，或者
* 至少有一块相邻（4 个方向之一）砖块稳定不会掉落时

给你一个数组 hits ，这是需要依次消除砖块的位置。每当消除 hits[i] = (rowi, coli) 位置上的砖块时，
对应位置的砖块（若存在）会消失，然后其他的砖块可能因为这一消除操作而掉落。
一旦砖块掉落，它会立即从网格中消失（即，它不会落在其他稳定的砖块上）。
返回一个数组 result ，其中 result[i] 表示第 i 次消除操作对应掉落的砖块数目。

注意，消除可能指向是没有砖块的空白位置，如果发生这种情况，则没有砖块掉落。

示例 1：
输入：grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]
输出：[2]
解释：
网格开始为：
[[1,0,0,0]，
 [1,1,1,0]]
消除 (1,0) 处砖块，得到网格：
[[1,0,0,0]
 [0,1,1,0]]
两个砖 (1,1), (1,2) 不再稳定，因为它们不再与顶部相连，也不再与另一个稳定的砖相邻，因此它们将掉落。得到网格：
[[1,0,0,0],
 [0,0,0,0]]
因此，结果为 [2] 。

示例 2：
输入：grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]
输出：[0,0]
解释：
网格开始为：
[[1,0,0,0],
 [1,1,0,0]]
消除 (1,1) 处的砖块，得到网格：
[[1,0,0,0],
 [1,0,0,0]]
剩下的砖都很稳定，所以不会掉落。网格保持不变：
[[1,0,0,0],
 [1,0,0,0]]
接下来消除 (1,0) 处加粗的砖块，得到网格：
[[1,0,0,0],
 [0,0,0,0]]
剩下的砖块仍然是稳定的，所以不会有砖块掉落。
因此，结果为 [0,0] 。

提示：
* m == grid.length
* n == grid[i].length
* 1 <= m, n <= 200
* grid[i][j] 为 0 或 1
* 1 <= hits.length <= 4 * 10^4
* hits[i].length == 2
* 0 <= xi <= m - 1
* 0 <= yi <= n - 1
* 所有 (xi, yi) 互不相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bricks-falling-when-hit
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：并查集
"""

from typing import List, Tuple


class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        # 思路：反向思考，将砖块填补上，计算每次填补后有多少砖块变得稳定

        # 初始化砖块状态 -> curGrid
        m, n = len(grid), len(grid[0])
        for hit in hits:  # 隐藏被击落的砖块
            grid[hit[0]][hit[1]] -= 1

        # 初始化并查集 -> disjointSet
        disjointSet = [[None] * n for _ in range(m)]  # 并查集
        setCount = [[1] * n for _ in range(m)]  # [[集合大小（只有根节点有效）]]
        for i, row in enumerate(grid):
            for j in range(1, n):
                if row[j - 1] == row[j] == 1:
                    self._merge(disjointSet, setCount, i, j - 1, i, j)
        for j in range(n):
            for i in range(1, m):
                if grid[i - 1][j] == grid[i][j] == 1:
                    self._merge(disjointSet, setCount, i - 1, j, i, j)

        # 逆向填补砖块
        result = []
        for hit in reversed(hits):
            hx, hy = hit[0], hit[1]
            grid[hx][hy] += 1
            mergedCount = 0
            if grid[hx][hy] == 1:
                if hx > 0 and grid[hx - 1][hy] == 1:  # 向上合并
                    mergedCount += self._merge(disjointSet, setCount, hx, hy, hx - 1, hy)
                if hx + 1 < m and grid[hx + 1][hy] == 1:  # 向下合并
                    mergedCount += self._merge(disjointSet, setCount, hx, hy, hx + 1, hy)
                if hy > 0 and grid[hx][hy - 1] == 1:  # 向左合并
                    mergedCount += self._merge(disjointSet, setCount, hx, hy, hx, hy - 1)
                if hy + 1 < n and grid[hx][hy + 1] == 1:  # 向右合并
                    mergedCount += self._merge(disjointSet, setCount, hx, hy, hx, hy + 1)
            result.append(max(mergedCount - (hx != 0), 0))  # 注意当击落的砖块在第一行的计数区别
        result.reverse()
        return result

    def _getRoot(self, disjointSet, x: int, y: int) -> Tuple[int, int]:
        """ 获取(x,y)的根节点 """
        visiteds = []
        while disjointSet[x][y]:
            visiteds.append((x, y))
            x, y = disjointSet[x][y]
        for visited in visiteds:
            disjointSet[visited[0]][visited[1]] = (x, y)
        return x, y

    def _merge(self, disjointSet, setCount, x1: int, y1: int, x2: int, y2: int) -> int:
        """ 合并
        :returns: 因本次合并从不稳定变为稳定的砖块数
        """
        rx1, ry1 = self._getRoot(disjointSet, x1, y1)
        rx2, ry2 = self._getRoot(disjointSet, x2, y2)
        if rx1 == rx2 and ry1 == ry2:
            return 0
        if rx2 < rx1:
            rx1, ry1, rx2, ry2 = rx2, ry2, rx1, ry1
        disjointSet[rx2][ry2] = (rx1, ry1)
        mergedCount = setCount[rx2][ry2]
        setCount[rx1][ry1] += mergedCount
        return mergedCount if rx1 == 0 and rx2 != 0 else 0


if __name__ == '__main__':
    s = Solution()
    r = s.hitBricks([[1, 0, 0, 0], [1, 1, 1, 0]], [[1, 0]])
    print(r)
    r = s.hitBricks([[1, 0, 0, 0], [1, 1, 0, 0]], [[1, 1], [1, 0]])
    print(r)
