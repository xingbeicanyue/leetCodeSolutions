"""
最小路径和

给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。

示例 1：
输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。

示例 2：
输入：grid = [[1,2,3],[4,5,6]]
输出：12

提示：
* m == grid.length
* n == grid[i].length
* 1 <= m, n <= 200
* 0 <= grid[i][j] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数组、动态规划
"""

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        width = len(grid[0])
        lastLens = [0] + [20001] * (width - 1)
        for i, row in enumerate(grid):
            curLens = [lastLens[0] + row[0]]
            for j in range(1, width):
                curLens.append(min(curLens[j - 1], lastLens[j]) + row[j])
            lastLens = curLens
        return lastLens[-1]


if __name__ == '__main__':
    s = Solution()
    r = s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
    print(r)
    r = s.minPathSum([[1, 2, 3], [4, 5, 6]])
    print(r)
