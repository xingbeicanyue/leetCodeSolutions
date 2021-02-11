"""
搜索二维矩阵 II

编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
* 每行的元素从左到右升序排列。
* 每列的元素从上到下升序排列。

示例 1：
输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
输出：true

示例 2：
输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
输出：false

提示：
* m == matrix.length
* n == matrix[i].length
* 1 <= n, m <= 300
* -10^9 <= matix[i][j] <= 10^9
* 每行的所有元素从左到右升序排列
* 每列的所有元素从上到下升序排列
* -10^9 <= target <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：二分查找、分治算法
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 从左下角开始，如果小于目标则上移，大于目标则右移
        curX, curY = len(matrix) - 1, 0
        while curX >= 0 and curY < len(matrix[0]):
            if matrix[curX][curY] == target:
                return True
            if matrix[curX][curY] < target:
                curY += 1
            else:
                curX -= 1
        return False


if __name__ == '__main__':
    s = Solution()
    r = s.searchMatrix(
        [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5)
    print(r)
    r = s.searchMatrix(
        [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20)
    print(r)
