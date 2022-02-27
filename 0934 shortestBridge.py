"""
最短的桥

在给定的二维二进制数组 A 中，存在两座岛。（岛是由四面相连的 1 形成的一个最大组。）

现在，我们可以将 0 变为 1，以使两座岛连接起来，变成一座岛。

返回必须翻转的 0 的最小数目。（可以保证答案至少是 1 。）

示例 1：
输入：A = [[0,1],[1,0]]
输出：1

示例 2：
输入：A = [[0,1,0],[0,0,0],[0,0,1]]
输出：2

示例 3：
输入：A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
输出：1

提示：
* 2 <= A.length == A[0].length <= 100
* A[i][j] == 0 或 A[i][j] == 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-bridge
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：深度优先搜索、广度优先搜索、数组、矩阵
"""

from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # 使用深度或广度优先遍历找到第一个岛屿的所有坐标
        # 从第一个岛屿的所有坐标开始广度遍历，第一次遇到第二个岛屿即为最短路径

        # 找到第一个岛屿 -> posQueue
        height, width = len(grid), len(grid[0])
        posStack = []
        for i, row in enumerate(grid):  #
            for j, ele in enumerate(row):
                if ele == 1:
                    posStack.append((i, j))
                    break
            if len(posStack) > 0:
                break
        posQueue = []  # [第一个岛屿的坐标]
        visitedss = [[False] * width for _ in range(height)]
        while posStack:
            pos = posStack.pop()
            if pos[0] < 0 or pos[0] >= height or pos[1] < 0 or pos[1] >= width or visitedss[pos[0]][pos[1]] or\
                    grid[pos[0]][pos[1]] == 0:
                continue
            visitedss[pos[0]][pos[1]] = True
            posQueue.append(pos)
            posStack.append((pos[0] + 1, pos[1]))
            posStack.append((pos[0] - 1, pos[1]))
            posStack.append((pos[0], pos[1] + 1))
            posStack.append((pos[0], pos[1] - 1))

        # 广度优先遍历
        result = -1
        visitedss = [[False] * width for _ in range(height)]
        while posQueue:
            nextQueue = []
            for pos in posQueue:
                if pos[0] < 0 or pos[0] >= height or pos[1] < 0 or pos[1] >= width or visitedss[pos[0]][pos[1]]:
                    continue
                if grid[pos[0]][pos[1]] == 1 and result > 0:
                    return result
                visitedss[pos[0]][pos[1]] = True
                nextQueue.append((pos[0] + 1, pos[1]))
                nextQueue.append((pos[0] - 1, pos[1]))
                nextQueue.append((pos[0], pos[1] + 1))
                nextQueue.append((pos[0], pos[1] - 1))
            posQueue = nextQueue
            result += 1
        return 0


if __name__ == '__main__':
    s = Solution()

    r = s.shortestBridge([[0, 1], [1, 0]])
    print(r)

    r = s.shortestBridge([[0, 1, 0], [0, 0, 0], [0, 0, 1]])
    print(r)

    r = s.shortestBridge([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]])
    print(r)
