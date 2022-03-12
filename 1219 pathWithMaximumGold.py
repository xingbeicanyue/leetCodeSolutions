"""
黄金矿工

你要开发一座金矿，地质勘测学家已经探明了这座金矿中的资源分布，并用大小为 m * n 的网格 grid 进行了标注。
每个单元格中的整数就表示这一单元格中的黄金数量；如果该单元格是空的，那么就是 0。

为了使收益最大化，矿工需要按以下规则来开采黄金：
* 每当矿工进入一个单元，就会收集该单元格中的所有黄金。
* 矿工每次可以从当前位置向上下左右四个方向走。
* 每个单元格只能被开采（进入）一次。
* 不得开采（进入）黄金数目为 0 的单元格。
* 矿工可以从网格中任意一个有黄金的单元格出发或者是停止。
 
示例 1：
输入：grid = [[0,6,0],[5,8,7],[0,9,0]]
输出：24
解释：
[[0,6,0],
 [5,8,7],
 [0,9,0]]
一种收集最多黄金的路线是：9 -> 8 -> 7。

示例 2：
输入：grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
输出：28
解释：
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
一种收集最多黄金的路线是：1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7。

提示：
* 1 <= grid.length, grid[i].length <= 15
* 0 <= grid[i][j] <= 100
* 最多 25 个单元格中有黄金。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-with-maximum-gold
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        def walk(x: int, y: int, gold: int) -> int:
            """ 探索grid[x][y]
            :returns: 返回所有分支中的最大黄金数
            """
            if not 0 <= x <= m - 1 or not 0 <= y <= n - 1 or grid[x][y] == 0 or visiteds[x][y]:
                return gold
            visiteds[x][y] = True
            gold += grid[x][y]
            result = max(walk(x - 1, y, gold), walk(x + 1, y, gold), walk(x, y - 1, gold), walk(x, y + 1, gold))
            visiteds[x][y] = False
            return result

        m, n = len(grid), len(grid[0])
        visiteds = [[False] * n for _ in range(m)]
        return max(walk(i, j, 0) for i in range(m) for j in range(n))


if __name__ == '__main__':
    s = Solution()
    r = s.getMaximumGold([[0, 6, 0], [5, 8, 7], [0, 9, 0]])
    print(r)
    r = s.getMaximumGold([[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]])
    print(r)
