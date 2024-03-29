"""
二维区域和检索 - 矩阵不可变

给定一个二维矩阵 matrix，以下类型的多个请求：
* 计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2) 。

实现 NumMatrix 类：
* NumMatrix(int[][] matrix) 给定整数矩阵 matrix 进行初始化
* int sumRegion(int row1, int col1, int row2, int col2) 返回左上角(row1, col1)、右下角(row2, col2)所描述的子矩阵的元素总和 。

示例 1：
输入:
["NumMatrix","sumRegion","sumRegion","sumRegion"]
[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]
输出:
[null, 8, 11, 12]

解释:
NumMatrix numMatrix = new NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8
numMatrix.sumRegion(1, 1, 2, 2); // return 11
numMatrix.sumRegion(1, 2, 2, 4); // return 12

提示：
* m == matrix.length
* n == matrix[i].length
* 1 <= m, n <= 200
* -10^5 <= matrix[i][j] <= 10^5
* 0 <= row1 <= row2 < m
* 0 <= col1 <= col2 < n
* 最多调用 10^4 次 sumRegion 方法

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-query-2d-immutable
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # 建立二维前缀和矩阵 -> self._sumss
        n = len(matrix[0])
        self._sumss = [[0] * (n + 1)]
        for row in matrix:
            sums = [0]
            sum_ = 0
            for i, num in enumerate(row):
                sum_ += num
                sums.append(sum_ + self._sumss[-1][i + 1])
            self._sumss.append(sums)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self._sumss[row2 + 1][col2 + 1] - self._sumss[row2 + 1][col1] - self._sumss[row1][col2 + 1] +\
               self._sumss[row1][col1]


if __name__ == '__main__':
    numMatrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    print(numMatrix.sumRegion(2, 1, 4, 3))
    print(numMatrix.sumRegion(1, 1, 2, 2))
    print(numMatrix.sumRegion(1, 2, 2, 4))
