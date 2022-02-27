"""
01 矩阵

给定一个由 0 和 1 组成的矩阵 mat，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。

两个相邻元素间的距离为 1 。

示例 1：
输入：mat = [[0,0,0],[0,1,0],[0,0,0]]
输出：[[0,0,0],[0,1,0],[0,0,0]]

示例 2：
输入：mat = [[0,0,0],[0,1,0],[1,1,1]]
输出：[[0,0,0],[0,1,0],[1,2,1]]

提示：
* m == mat.length
* n == mat[i].length
* 1 <= m, n <= 10^4
* 1 <= m * n <= 10^4
* mat[i][j] is either 0 or 1.
* mat 中至少有一个 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/01-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：广度优先搜索、数组、动态规划、矩阵
"""

from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # 从0所在的位置开始广度优先遍历
        height, width = len(mat), len(mat[0])
        result = [[-1] * width for _ in range(height)]
        curPoss = [(i, j) for i in range(height) for j in range(width) if mat[i][j] == 0]
        dist = 0
        while curPoss:
            nextPoss = []
            for curPos in curPoss:
                if result[curPos[0]][curPos[1]] < 0:
                    result[curPos[0]][curPos[1]] = dist
                    if curPos[0] > 0:
                        nextPoss.append((curPos[0] - 1, curPos[1]))
                    if curPos[0] < height - 1:
                        nextPoss.append((curPos[0] + 1, curPos[1]))
                    if curPos[1] > 0:
                        nextPoss.append((curPos[0], curPos[1] - 1))
                    if curPos[1] < width - 1:
                        nextPoss.append((curPos[0], curPos[1] + 1))
            curPoss = nextPoss
            dist += 1
        return result


if __name__ == '__main__':
    s = Solution()

    r = s.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    print(r)

    r = s.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]])
    print(r)
