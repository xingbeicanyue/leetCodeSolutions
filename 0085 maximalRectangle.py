"""
最大矩形

给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例 1：
 |-------------------|
 | 1 | 0 | 1 | 0 | 0 |
 | 1 | 0 |'1'|'1'|'1'|
 | 1 | 1 |'1'|'1'|'1'|
 | 1 | 0 | 0 | 1 | 0 |
 |-------------------|
输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：6
解释：最大矩形如上图所示。

示例 2：
输入：matrix = []
输出：0

示例 3：
输入：matrix = [["0"]]
输出：0

示例 4：
输入：matrix = [["1"]]
输出：1

示例 5：
输入：matrix = [["0","0"]]
输出：0
 
提示：
* rows == matrix.length
* cols == matrix[0].length
* 0 <= row, cols <= 200
* matrix[i][j] 为 '0' 或 '1'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximal-rectangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：栈、数组、哈希表、动态规划
"""

from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # 计算每行中每个格子向上的最长连通数，再使用#84的方法
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        result = 0
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        for i in range(rows):
            heights = [heights[j] * int(matrix[i][j]) + int(matrix[i][j]) for j in range(cols)]
            lefts, rights = [-1] * cols, [cols] * cols
            limits = []
            for j in range(cols):
                while limits:
                    if heights[j] <= limits[-1][0]:
                        rights[limits.pop()[1]] = j
                    else:
                        lefts[j] = limits[-1][1]
                        break
                limits.append((heights[j], j))
            result = max(result, max((rights[j] - lefts[j] - 1) * heights[j] for j in range(cols)))
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.maximalRectangle(
        [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]])
    print(r)
    r = s.maximalRectangle([])
    print(r)
    r = s.maximalRectangle([["0"]])
    print(r)
    r = s.maximalRectangle([["1"]])
    print(r)
    r = s.maximalRectangle([["0", "0"]])
    print(r)
