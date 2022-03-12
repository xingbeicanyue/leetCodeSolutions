"""
最大正方形

在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。

示例 1：
输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：4

示例 2：
输入：matrix = [["0","1"],["1","0"]]
输出：1

示例 3：
输入：matrix = [["0"]]
输出：0

提示：
* m == matrix.length
* n == matrix[i].length
* 1 <= m, n <= 300
* matrix[i][j] 为 '0' 或 '1'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximal-square
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 方法1：
        # 动态规划
        # 设S(i,j)为以matrix[i][j]为右下角的最大正方形边长，则S(i,j) = min(S(i-1,j) + S(i,j-1) + S(i-1,j-1)) + 1
        result, width = 0, len(matrix[0])
        lastMaxSideLen = [0] * width  # [上一行 以该坐标为右下角的最大正方形边长]
        for i, row in enumerate(matrix):
            curMaxSideLen = [0] * width  # [本行 以该坐标为右下角的最大正方形边长]
            for j, ele in enumerate(row):
                if ele == '1':
                    # j = 0 也没问题
                    curMaxSideLen[j] = min(lastMaxSideLen[j - 1], lastMaxSideLen[j], curMaxSideLen[j - 1]) + 1
                    result = max(result, curMaxSideLen[j])
            lastMaxSideLen = curMaxSideLen
        return result * result


        # 方法2：
        # 类似#85的思路，逐行求向上的最长连通数，然后求最大正方形面积
        # result, width = 0, len(matrix[0])
        # lastHeights = [0] * width  # [上一行向上最长连通数]
        # for row in matrix:
        #     # 本行向上最长连通数
        #     curHeights = [lastHeights[i] + 1 if ele == '1' else 0 for i, ele in enumerate(row)]
        #     limits = []  # [(高度, 能满足该高度矩形的左侧起始下标)]
        #     for i, height in enumerate(curHeights):
        #         leftIdx = None
        #         while limits:
        #             if height >= limits[-1][0]:
        #                 break
        #             popHeight, leftIdx = limits.pop()
        #             result = max(result, min(i - leftIdx, popHeight))
        #         limits.append((height, i if leftIdx is None else leftIdx))
        #     for limit in limits:
        #         result = max(result, min(width - limit[1], limit[0]))
        #     lastHeights = curHeights
        # return result * result


if __name__ == '__main__':
    s = Solution()

    r = s.maximalSquare(
        [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]])
    print(r)

    r = s.maximalSquare([["0", "1"], ["1", "0"]])
    print(r)

    r = s.maximalSquare([["0"]])
    print(r)
