"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

--------------------------------------------------
|Start |      |      |      |      |      |      |
--------------------------------------------------
|      |      |      |      |      |      |      |
--------------------------------------------------
|      |      |      |      |      |      |Finish|
--------------------------------------------------

网格中的障碍物和空位置分别用 1 和 0 来表示。

示例 1：
----------------------
|Start |      |      |
----------------------
|      |   X  |      |
----------------------
|      |      |Finish|
----------------------
输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2
解释：
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右

示例 2：
---------------
|Start |   X  |
---------------
|      |Finish|
---------------
输入：obstacleGrid = [[0,1],[0,0]]
输出：1
 
提示：
* m == obstacleGrid.length
* n == obstacleGrid[i].length
* 1 <= m, n <= 100
* obstacleGrid[i][j] 为 0 或 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数组、动态规划
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        pathCountss = [[1] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        for j in range(1, len(pathCountss[0])):
            pathCountss[0][j] = 0 if pathCountss[0][j - 1] == 0 or obstacleGrid[0][j] == 1 else 1
        for i in range(1, len(pathCountss)):
            pathCountss[i][0] = 0 if pathCountss[i - 1][0] == 0 or obstacleGrid[i][0] == 1 else 1
        for i in range(1, len(pathCountss)):
            for j in range(1, len(pathCountss[i])):
                if obstacleGrid[i][j] == 1:
                    pathCountss[i][j] = 0
                else:
                    pathCountss[i][j] = pathCountss[i - 1][j] + pathCountss[i][j - 1]
        return pathCountss[-1][-1]


if __name__ == '__main__':
    s = Solution()
    result = s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    print(result)
    result = s.uniquePathsWithObstacles([[0, 1], [0, 0]])
    print(result)
